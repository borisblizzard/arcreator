#ifndef REACTOR_INPUT_H
#define REACTOR_INPUT_H

#include <april/InputDelegate.h>
#include <april/Keys.h>
#include <gtypes/Vector2.h>
#include <hltypes/harray.h>
#include <hltypes/hltypesUtil.h>
#include <hltypes/hstring.h>

#define REACTOR_INPUT_MAX_KEYS 256
#define REACTOR_INPUT_MAX_BUTTONS 256
#define REACTOR_INPUT_STATE_DEFAULT "Reactor:Default"
#define REACTOR_INPUT_STATE_MESSAGE "Reactor:Message"
#define REACTOR_INPUT_STATE_WAIT "Reactor:Wait"

namespace reactor
{
	class Input : public april::InputDelegate
	{
	public:
		enum PressState
		{
			ACTIVE,
			INACTIVE,
			ACTIVATED,
			DEACTIVATED
		};
			
		enum InputState
		{
			IDLE,
			TRIGGER,
			PRESS,
			RELEASE
		};
			
		Input();
		~Input();
			
		gvec2 getCursorPosition();
		HL_DEFINE_GETSET(harray<april::Key>, confirmKeys, ConfirmKeys);
		HL_DEFINE_GETSET(harray<april::Key>, cancelKeys, CancelKeys);
		HL_DEFINE_GETSET(harray<april::Button>, confirmButtons, ConfirmButtons);
		HL_DEFINE_GETSET(harray<april::Button>, cancelButtons, CancelButtons);
			
		void update();
		void reset();
			
		bool isMouseTriggered();
		bool isMouseTriggered(april::Key keyCode);
		bool isMousePressed();
		bool isMousePressed(april::Key keyCode);
		bool isMouseReleased();
		bool isMouseReleased(april::Key keyCode);
			
		bool isKeyTriggered(april::Key keyCode);
		bool isKeyPressed(april::Key keyCode);
		bool isKeyReleased(april::Key keyCode);
		bool isButtonTriggered(april::Button buttonCode);
		bool isButtonPressed(april::Button buttonCode);
		bool isButtonReleased(april::Button buttonCode);
			
		void addState(chstr newState);
		hstr removeState();
		hstr getCurrentState();
		void resetState();
			
		void addKey(april::Key keyCode);
		void addButton(april::Button buttonCode);
			
		void onMouseDown(april::Key keyCode);
		void onMouseUp(april::Key keyCode);
		void onMouseCancel(april::Key keyCode);
		void onMouseMove();
		void onMouseScroll(float x, float y);
		void onKeyDown(april::Key keyCode);
		void onKeyUp(april::Key keyCode);
		void onChar(unsigned int charCode);
		void onTouch(const harray<gvec2>& touches);
		void onButtonDown(april::Button buttonCode);
		void onButtonUp(april::Button buttonCode);
			
	protected:
		harray<hstr> stateStack;
		PressState mouseDown;
		InputState mouseState;
		PressState keyDowns[REACTOR_INPUT_MAX_KEYS];
		InputState keyStates[REACTOR_INPUT_MAX_KEYS];
		PressState buttonDowns[REACTOR_INPUT_MAX_BUTTONS];
		InputState buttonStates[REACTOR_INPUT_MAX_BUTTONS];
			
		harray<april::Key> controlKeys;
		harray<april::Button> controlButtons;
			
		harray<april::Key> confirmKeys;
		harray<april::Key> cancelKeys;
		harray<april::Button> confirmButtons;
		harray<april::Button> cancelButtons;

	};
	
	extern Input* input;
	
}
#endif
