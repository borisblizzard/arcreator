#ifndef SYSTEM_CONTEXT_H
#define SYSTEM_CONTEXT_H

#include <gtypes/Vector2.h>
#include <hltypes/harray.h>

#define MAX_KEYS 256

namespace System
{
	class Context
	{
	public:
		enum MouseState
		{
			IDLE,
			TRIGGER,
			PRESS,
			RELEASE
		};

		enum State
		{
			DEFAULT
		};
		
		Context();
		~Context();
		State getState();
		void setState(State value);

		void update();
		void reset();
		void onMouseDown(float x, float y, int button);
		void onMouseUp(float x, float y, int button);
		void onMouseMove(float x, float y);
		void onKeyDown(unsigned int keycode);
		void onKeyUp(unsigned int keycode);
		void onChar(unsigned int charcode);
		
		bool isMouseTriggered();
		bool isMousePressed();
		bool isMouseReleased();
		
		bool isKeyTriggered(unsigned int keycode);
		bool isKeyPressed(unsigned int keycode);
		bool isKeyReleased(unsigned int keycode);
		
		void setPrevious();

	private:
		harray<State> states;
		MouseState mouse;
		harray<unsigned int> controlKeys;
		bool triggered[MAX_KEYS];
		bool pressed[MAX_KEYS];
		bool released[MAX_KEYS];
		bool keys[MAX_KEYS];
		
	};
	
	extern Context* context;
	
}
#endif
