#pragma once

#include<require.hpp>
#include<path.hpp>
#include<python.hpp>



namespace Python_Core{
	// ~~~~~~~~~~~~ Define ~~~~~~~~~~~~
	bool exiting = false;
	bool restarting = false;


	void setup();
	PyObject* PyInit_Core();

	PyObject* home(PyObject*, PyObject*);

	PyObject* programName(PyObject*, PyObject*);
	PyObject* programFile(PyObject*, PyObject*);

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

		{"programName", programName, METH_NOARGS, ""},
		{"programFile", programFile, METH_NOARGS, ""},

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
	PyObject* PyInit_Core(){
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


	PyObject* programName(PyObject *self, PyObject *args){
		return PyUnicode_FromString(PROGRAM_NAME);
	}

	PyObject* programFile(PyObject *self, PyObject *args){
		return PyUnicode_FromString(PROGRAM_FILE);
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
				Python_Core::exiting = val;
			}
		}

		if (Python_Core::exiting){
			Py_RETURN_TRUE;
		} else {
			Py_RETURN_FALSE;
		}
	}


	PyObject* isRestarting(PyObject *self, PyObject *args){
		u_char val = 2;

		if (PyArg_ParseTuple(args, "|p", &val)){
			if (val != 2){
				Python_Core::restarting = val;
			}
		}

		if (Python_Core::restarting){
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
