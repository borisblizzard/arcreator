#ifndef ZER0_CONTEXT_H
#define ZER0_CONTEXT_H

#include <gtypes/Vector2.h>
#include <hltypes/harray.h>

#define MAX_KEYS 256

namespace zer0
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
		
		bool isMouseTriggered();
		bool isMousePressed();
		bool isMouseReleased();
		
		bool isKeyTriggered(unsigned int keycode);
		bool isKeyPressed(unsigned int keycode);
		bool isKeyReleased(unsigned int keycode);
		
		void setPrevious();

		static void onMouseDown(float x, float y, int button);
		static void onMouseUp(float x, float y, int button);
		static void onMouseMove(float x, float y);
		static void onKeyDown(unsigned int keycode);
		static void onKeyUp(unsigned int keycode);
		static void onChar(unsigned int charcode);

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
