#include<require.hpp>
#include<path.hpp>
#include<startup.hpp>

#include<python.hpp>
#include<python_core.hpp>



int main(int argC, char* argV[]){
	Path::setup();
	Startup::setup();


	Python::setupPreConfig(argC, argV);
	Python::setupConfig();

	Python::runMain();

	Python::finalize();

	Python::runRestart();

	
	return 0x00;
}


