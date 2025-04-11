#pragma once


#define PROGRAM_FILE_WINDOWED "DesktopDisplay.exe"
#define PROGRAM_FILE_DEBUG "DesktopDisplay_Debug.exe"
#define PROGRAM_FILE_TASK "DesktopDisplay_Task.exe"



// ~~~~~~~~~ Program Name ~~~~~~~~~
#ifdef DEBUG
	#ifdef TASK
		#define PROGRAM_NAME "DesktopDisplay Task"
	#else
		#define PROGRAM_NAME "DesktopDisplay Debug"
	#endif
#else
	#define PROGRAM_NAME "DesktopDisplay"
#endif
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


// ~~~~~~~~~ Program File ~~~~~~~~~
#ifdef DEBUG
	#ifdef TASK
		#define PROGRAM_FILE PROGRAM_FILE_TASK
	#else
		#define PROGRAM_FILE PROGRAM_FILE_DEBUG
	#endif
#else
	#define PROGRAM_FILE PROGRAM_FILE_WINDOWED
#endif
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


// ~~~~~~~~~ Program Icon ~~~~~~~~~
#ifdef DEBUG
	#ifdef TASK
		#define PROGRAM_ICON "icon_task.ico"
	#else
		#define PROGRAM_ICON "icon_debug.ico"
	#endif
#else
	#define PROGRAM_ICON "icon.ico"
#endif
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#define COMPANY_NAME "Atlis"
#define PROGRAM_COPYRIGHT "Copyright (C) Atlis"

#define PROGRAM_VERSION "1.0.0"
#define PROGRAM_VERSION_ID 1,0,0


