#include<require.hpp>
#include<path.hpp>
#include<python.hpp>
#include<startup.hpp>





int main(int argC, char* argV[]){
	Path::setup();
	Startup::setup();


	Python::setupPreConfig();
	Python::setupConfig(argC, argV);


	{
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
				
				} else if (result == Py_True){
					// Restart program
					execve(
						Path::exePath.string().c_str(),
						argV,
						NULL
					);
				}
			}

			Py_DECREF(mod);
			Py_DECREF(func);
		} else {
			PyErr_Print();
		}
	}


	Python::finalize();


	return 0x00;
}


