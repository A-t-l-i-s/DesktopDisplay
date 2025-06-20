#pragma once

#include<require.hpp>
#include<path.hpp>
#include<python.hpp>



namespace Python_Internal{
	// ~~~~~~~~~~~~ Define ~~~~~~~~~~~~
	bool exiting = false;
	bool restarting = false;


	void setup();
	PyObject* PyInit_Internal();

	PyObject* home(PyObject*, PyObject*);

	PyObject* isStartup(PyObject*, PyObject*);

	PyObject* programName(PyObject*, PyObject*);
	PyObject* programFile(PyObject*, PyObject*);
	PyObject* programVersion(PyObject*, PyObject*);

	PyObject* programFileWindowed(PyObject*, PyObject*);
	PyObject* programFileDebug(PyObject*, PyObject*);
	PyObject* programFileTask(PyObject*, PyObject*);

	PyObject* isDebug(PyObject*, PyObject*);
	PyObject* isTask(PyObject*, PyObject*);
	PyObject* isProduction(PyObject*, PyObject*);

	PyObject* isExiting(PyObject*, PyObject*);
	PyObject* isRestarting(PyObject*, PyObject*);

	PyObject* pid(PyObject*, PyObject*);
	// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	// ~~~~~~~ Methods Structure ~~~~~~
	static PyMethodDef pyMethods[] = {
		{"home", home, METH_NOARGS, ""},

		{"isStartup", isStartup, METH_VARARGS, ""},

		{"programName", programName, METH_NOARGS, ""},
		{"programFile", programFile, METH_NOARGS, ""},
		{"programVersion", programVersion, METH_NOARGS, ""},

		{"programFileWindowed", programFileWindowed, METH_NOARGS, ""},
		{"programFileDebug", programFileDebug, METH_NOARGS, ""},
		{"programFileTask", programFileTask, METH_NOARGS, ""},

		{"isDebug", isDebug, METH_NOARGS, ""},
		{"isTask", isTask, METH_NOARGS, ""},
		{"isProduction", isProduction, METH_NOARGS, ""},

		{"isExiting", isExiting, METH_VARARGS, ""},
		{"isRestarting", isRestarting, METH_VARARGS, ""},

		{"pid", pid, METH_NOARGS, ""},

	{NULL, NULL, 0, NULL}};
	// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	// ~~~~~~~ Module Structure ~~~~~~~
	static PyModuleDef pyModule = {
		PyModuleDef_HEAD_INIT,
		"Core",
		NULL,
		-1,
		pyMethods
	};
	// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	// ~~~~~~~~~~ Initializer ~~~~~~~~~
	PyObject* PyInit_Internal(){
		return PyModule_Create(&pyModule);
	}
	// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	// ~~~~~~~~ Module Methods ~~~~~~~~
	PyObject* home(PyObject *self, PyObject *args){
		return Py_BuildValue(
			"s",
			Path::programPath.generic_string().c_str()
		);
	}


	PyObject* isStartup(PyObject *self, PyObject *args){
		u_char val = 2;

		if (PyArg_ParseTuple(args, "|p", &val)){
			#if defined(PRODUCTION) && not defined(DEBUG) && not defined(TASK)
				bool isValid = false;
				HKEY hKey;
				LONG result;

				result = RegOpenKeyExA(
					HKEY_CURRENT_USER,
					PROGRAM_REGEX,
					0, 
					KEY_ALL_ACCESS,
					&hKey
				);

				if (result == ERROR_SUCCESS){
					if (val == true){
						string path = "\"" + Path::exePath.generic_string() + "\"";

						uint16_t size = path.size();
						const uint8_t* value = (const uint8_t*)path.c_str();

						// Add value to registry
						RegSetValueExA(
							hKey,
							PROGRAM_REGEX_NAME,
							0,
							REG_SZ,
							value,
							size
						);

					} else if (val == false){
						// Delete registry
						RegDeleteValue(
							hKey,
							PROGRAM_REGEX_NAME
						);
					}

					if (RegGetValueA(hKey, NULL, PROGRAM_REGEX_NAME, RRF_RT_ANY, NULL, NULL, NULL) == ERROR_SUCCESS){
						isValid = true;
					}

					// Close key
					RegCloseKey(hKey);
				}

				if (isValid){
					Py_RETURN_TRUE;
				}
			#endif
		}


		Py_RETURN_FALSE;
	}


	PyObject* programName(PyObject *self, PyObject *args){
		return PyUnicode_FromString(PROGRAM_NAME);
	}

	PyObject* programFile(PyObject *self, PyObject *args){
		return PyUnicode_FromString(PROGRAM_FILE);
	}

	PyObject* programVersion(PyObject *self, PyObject *args){
		return PyUnicode_FromString(PROGRAM_VERSION);
	}


	PyObject* programFileWindowed(PyObject *self, PyObject *args){
		return PyUnicode_FromString(PROGRAM_FILE_WINDOWED);
	}

	PyObject* programFileDebug(PyObject *self, PyObject *args){
		return PyUnicode_FromString(PROGRAM_FILE_DEBUG);
	}

	PyObject* programFileTask(PyObject *self, PyObject *args){
		return PyUnicode_FromString(PROGRAM_FILE_TASK);
	}


	PyObject* isDebug(PyObject *self, PyObject *args){
		#ifdef DEBUG
			Py_RETURN_TRUE;
		#else
			Py_RETURN_FALSE;
		#endif
	}

	PyObject* isTask(PyObject *self, PyObject *args){
		#ifdef TASK
			Py_RETURN_TRUE;
		#else
			Py_RETURN_FALSE;
		#endif
	}

	PyObject* isProduction(PyObject *self, PyObject *args){
		#ifdef PRODUCTION
			Py_RETURN_TRUE;
		#else
			Py_RETURN_FALSE;
		#endif
	}


	PyObject* isExiting(PyObject *self, PyObject *args){
		u_char val = 2;

		if (PyArg_ParseTuple(args, "|p", &val)){
			if (val != 2){
				Python_Internal::exiting = val;
			}
		}

		if (Python_Internal::exiting){
			Py_RETURN_TRUE;
		} else {
			Py_RETURN_FALSE;
		}
	}


	PyObject* isRestarting(PyObject *self, PyObject *args){
		u_char val = 2;

		if (PyArg_ParseTuple(args, "|p", &val)){
			if (val != 2){
				Python_Internal::restarting = val;
			}
		}

		if (Python_Internal::restarting){
			Py_RETURN_TRUE;
		} else {
			Py_RETURN_FALSE;
		}
	}


	PyObject* pid(PyObject *self, PyObject *args){
		return Py_BuildValue(
			"i",
			getpid()
		);
	}
	// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
}
