#ifndef ZER0_SYSTEM_H
#define ZER0_SYSTEM_H

#include <hltypes/hstring.h>

namespace aprilui
{
	class EventArgs;
}

namespace zer0
{
	class System
	{
	public:
		System(chstr path);
		~System();
		
		hstr Path;
		float Time;
		bool Exiting;
		bool Focused;
		
		static bool onQuit(bool canCancel);
		static void onFocusChange(bool focused);
		
	};
	
	extern System* system;
	
}
#endif
