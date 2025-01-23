#pragma once

#include<require.hpp>
#include<path.hpp>



namespace Python{
	// ~~~~~~~~~~~ Variables ~~~~~~~~~~
	PyObject* mainModule;
	PyObject* mainGlobals;
	PyObject* mainLocals;
	// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	// ~~~~~~~~~~~~ Define ~~~~~~~~~~~~
	void setupPreConfig();
	void setupConfig(int, char**);

	bool runScript(fs::path, PyObject*, PyObject*);
	
	void finalize();
	// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	void setupPreConfig(){
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



	void setupConfig(int argC, char** argV){
		if (not Py_IsInitialized()){
			// Create python config
			PyConfig config;
			PyConfig_InitIsolatedConfig(&config);

			// Config
			config.write_bytecode = false;
			config.optimization_level = 0;
			config.program_name = (wchar_t*)programName;
			
			config.home = Path::childW("").data();
			config.pythonpath_env = Path::childW("").data();
			config.platlibdir = Path::childW("bin").data();

			config.safe_path = true;
			config.parse_argv = false;
			config.interactive = false;
			config.site_import = false;
			config.buffered_stdio = false;
			config.use_environment = false;
			config.configure_c_stdio = false;
			config.user_site_directory = false;

			// Prefix
			config.prefix = (wchar_t*)L".";

			// Parse args to python
			PyConfig_SetBytesArgv(&config, argC, argV);


			// Logging
			// config.verbose = true;
			// config.tracemalloc = true;


			// Add module search paths
			PyWideStringList_Append(&config.module_search_paths, Path::childW("bin").c_str());
			PyWideStringList_Append(&config.module_search_paths, Path::childW("lib").c_str());
			PyWideStringList_Append(&config.module_search_paths, Path::childW("lib.zip").c_str());

			// Prevent module paths from override
			config.module_search_paths_set = true;


			// Initialize python
			PyStatus status = Py_InitializeFromConfig(&config);

			if (PyStatus_Exception(status)){
				Py_ExitStatusException(status);
			}


			// Import main module and get globals and locals
			mainModule = PyImport_AddModule("__main__");
			mainGlobals = PyModule_GetDict(mainModule);
			mainLocals = PyDict_New();
			

			PyDict_SetItemString(
				mainGlobals,
				"__name__",
				Py_BuildValue(
					"s",
					"__RyfterMain__"
				)
			);
		}
	}



	bool runScript(fs::path path, PyObject* globals, PyObject* locals){
		if (Py_IsInitialized()){
			if (fs::is_regular_file(path)){
				// Open file
				FILE* file = _Py_fopen_obj(
					Py_BuildValue("s", path.string().c_str()),
					"rb"
				);


				if (file != NULL){
					// Compile script
					PyObject* result = PyRun_FileExFlags(
						file,
						path.string().c_str(),
						Py_file_input,
						globals,
						locals,
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
					} else {
						return true;
					}
				}
			}
		}

		return false;
	}



	void finalize(){
		if (Py_IsInitialized()){
			// De-Initialize python
			Py_FinalizeEx();
		}
	}
}
