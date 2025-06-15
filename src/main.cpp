#include<require.hpp>
#include<path.hpp>
#include<python.hpp>
#include<python_internal.hpp>



int main(int argC, char* argV[]){
	Path::setup();

	Python::setupPreConfig(argC, argV);
	Python::setupConfig();

	Python::runMain();

	Python::finalize();

	Python::runRestart();

	
	return 0x00;
}


