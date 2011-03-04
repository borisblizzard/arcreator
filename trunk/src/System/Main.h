#ifndef SYSTEM_MAIN_H
#define SYSTEM_MAIN_H

#include <hltypes/hstring.h>

namespace aprilui
{
	class EventArgs;
}

namespace System
{
	class Main
	{
	public:
		Main();
		~Main();
		
		float Time;
		
		bool update(float k);
		bool exitGame();
		
		static void onMouseDown(float x, float y, int button);
		static void onMouseUp(float x, float y, int button);
		static void onMouseMove(float x, float y);
		static void onKeyDown(unsigned int keycode);
		static void onKeyUp(unsigned int keycode);
		static void onChar(unsigned int charcode);
		static bool onQuit(bool canCancel);
		static void onFocusChange(bool focused);
		
	protected:
		bool exiting;
		bool focused;

		bool _update();
		
	};
	
	void create();
	void init();
	void clear();
	void destroy();
	
	extern Main* main;
	extern hstr path;
	
}
#endif
