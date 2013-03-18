#ifndef REACTOR_SYSTEM_H
#define REACTOR_SYSTEM_H

#include <hltypes/hmap.h>
#include <hltypes/hstring.h>

namespace aprilui
{
	class EventArgs;
}

namespace reactor
{
	class System
	{
	public:
		System();
		~System();
		
		hstr Path;
		hmap<hstr, hstr> Parameters;
		hstr Title;
		float Time;
		bool Exiting;
		bool Focused;
		
		static bool onQuit(bool canCancel);
		static void onFocusChange(bool focused);

	protected:
		hmap<hstr, hstr> _readCfgFile(chstr filename);
		hstr _setupSystemPath(chstr title);

	};
	
	extern System* system;
	
}
#endif
