#pragma once

#include<require.hpp>
#include<path.hpp>
#include<python_core.hpp>



namespace Python{
	// ~~~~~~~~~~~ Variables ~~~~~~~~~~
	PyObject* mainModule;
	PyObject* mainGlobals;
	PyObject* mainLocals;

	int argC;
	char** argV;
	// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	// ~~~~~~~~~~~~ Define ~~~~~~~~~~~~
	void setupPreConfig(int, char**);
	void setupConfig();
	
	void finalize();

	void runMain();
	void runRestart();
	// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	void setupPreConfig(int argC, char** argV){
		Python::argC = argC;
		Python::argV = argV;

		if (not Py_IsInitialized()){
			// Create python pre config
			PyPreConfig config;
			PyPreConfig_InitIsolatedConfig(&config);

			// Config
			config.allocator = PYMEM_ALLOCATOR_DEFAULT;
			config.configure_locale = false;
			config.coerce_c_locale = false;
			config.coerce_c_locale_warn = false;
			config.dev_mode = false;
			config.isolated = true;
			config.parse_argv = false;
			config.use_environment = false;
			config.utf8_mode = true;


			// Pre initialize python
			PyStatus status = Py_PreInitialize(&config);

			if (PyStatus_Exception(status)){
				Py_ExitStatusException(status);
			}
		}
	}


	void setupConfig(){
		if (not Py_IsInitialized()){
			// Create python config
			PyConfig config;
			PyConfig_InitIsolatedConfig(&config);

			// Config
			config.write_bytecode = false;
			config.optimization_level = 0;
			config.program_name = (wchar_t*)PROGRAM_NAME;
			
			config.home = NULL;
			config.pythonpath_env = NULL;
			config.platlibdir = (wchar_t*)L"bin";

			config.safe_path = true;
			config.parse_argv = false;
			config.interactive = false;
			config.site_import = false;
			config.buffered_stdio = false;
			config.use_environment = false;
			config.configure_c_stdio = true;
			config.user_site_directory = false;

			// Prefix
			config.prefix = NULL;

			// Parse args to python
			PyConfig_SetBytesArgv(
				&config,
				Python::argC,
				Python::argV
			);


			// Logging
			#if defined(PRODUCTION) && defined(DEBUG) && not defined(TASK)
				config.verbose = true;
				config.tracemalloc = true;
			#else
				config.verbose = false;
				config.tracemalloc = false;
			#endif


			// Add module search paths
			PyWideStringList_Append(&config.module_search_paths, L"bin");
			PyWideStringList_Append(&config.module_search_paths, L"lib");
			PyWideStringList_Append(&config.module_search_paths, L"lib.zip");

			PyWideStringList_Append(&config.module_search_paths, L"res/lib");


			// Prevent module paths from override
			config.module_search_paths_set = true;


			PyImport_AppendInittab(
				"Core",
				Python_Core::PyInit_Core
			);


			// Initialize python
			PyStatus status = Py_InitializeFromConfig(&config);

			if (PyStatus_Exception(status)){
				Py_ExitStatusException(status);
			}


			// Import main module and get globals and locals
			mainModule = PyImport_AddModule("__main__");
			mainGlobals = PyModule_GetDict(mainModule);
			mainLocals = PyDict_New();
			

			{
				#ifdef TASK
					#define NAME "__DDTask__"
				#else
					#define NAME "__DDMain__"
				#endif

				PyDict_SetItemString(
					mainGlobals,
					"__name__",
					Py_BuildValue(
						"s",
						NAME
					)
				);
			}
		}
	}


	void finalize(){
		if (Py_IsInitialized()){
			// De-Initialize python
			Py_FinalizeEx();
		}
	}


	void runMain(){
		#ifndef TASK
			PyObject* mod = PyImport_ImportModuleEx(
				"main",
				Python::mainGlobals,
				Python::mainLocals,
				NULL
			);

			if (mod != NULL){
				PyObject* func = PyObject_GetAttrString(mod, "main");


				if (PyCallable_Check(func)){
					PyObject* result = PyObject_CallNoArgs(func);

					// Check if script raised any exception
					if (result == NULL){
						// Print exception
						PyErr_Print();
					}
				}

				Py_DECREF(mod);
				Py_DECREF(func);

			} else {
				PyErr_Print();
			}
		#else
			if (Python::argC > 1){
				string pathStr = Python::argV[1];
				fs::path path = fs::path(pathStr);

				if (fs::is_regular_file(path)){
					// Open file
					FILE* file = _Py_fopen_obj(
						Py_BuildValue("s", path.generic_string().c_str()),
						"rb"
					);


					{
						pid_t pid = getpid();
						string pidStr = std::to_string(pid);

						fs::path instPath = "insts";
						instPath /= pidStr;

						std::ofstream file(instPath, std::ios::binary | std::ios::out);

						string name;

						if (Python::argC > 2){
							name = Python::argV[2];
						} else {
							name = path.generic_string();
						}

						time_t t = time(NULL);
						string timeStr = std::to_string(t);


						file << name;
						file << "\x01";
						file << pidStr;
						file << "\x01";
						file << timeStr;

						file.close();
					}


					if (file != NULL){
						// Compile script
						PyObject* result = PyRun_FileExFlags(
							file,
							path.generic_string().c_str(),
							Py_file_input,
							Python::mainGlobals,
							Python::mainLocals,
							false,
							NULL
						);


						// Close file
						fclose(file);
						Py_DECREF(file);


						// Check if script raised any exception
						if (not result){
							// Print exception
							PyErr_Print();
						}
					}
				}
			}
		#endif
	}


	void runRestart(){
		if (Python_Core::restarting){
			#ifndef TASK
				execve(
					PROGRAM_FILE,
					Python::argV,
					NULL
				);

			#else
				string fName = "";
				string name = PROGRAM_FILE_TASK;

				if (Python::argC > 1){
					fName = "\"" + string(Python::argV[1]) + "\"";

					if (Python::argC > 2){
						name = "\"" + string(Python::argV[2]) + "\"";
					} else {
						name = PROGRAM_FILE_TASK;
					}
				}


				char* argVNew[4] = {
					Python::argV[0],
					fName.data(),
					name.data(),
					NULL
				};


				execve(
					PROGRAM_FILE,
					argVNew,
					NULL
				);
			#endif
		}
	}
}
