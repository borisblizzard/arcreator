#include <april/Keys.h>
#include <april/Window.h>
#include <gtypes/Vector2.h>
#include <hltypes/harray.h>
#include <hltypes/hlog.h>
#include <hltypes/hstring.h>

#include "Input.h"

namespace reactor
{
	Input* input = NULL;
	
	/****************************************************************************************
		* Construct/Destruct
		****************************************************************************************/
		
	Input::Input() : april::InputDelegate() // not initializing any variables, reset() takes care of that
	{
		this->reset();
		this->confirmKeys += april::AK_RETURN;
		this->cancelKeys += april::AK_ESCAPE;
	}
		
	Input::~Input()
	{
	}
		
	/****************************************************************************************
	 * Properties
	 ****************************************************************************************/
		
	gvec2 Input::getCursorPosition()
	{
		return april::window->getCursorPosition();
	}
		
	/****************************************************************************************
	 * Update
	 ****************************************************************************************/
		
	void Input::update()
	{
		// mouse input update
		if (this->mouseDown == ACTIVATED)
		{
			this->mouseDown = ACTIVE;
		}
		if (this->mouseDown == ACTIVE || this->mouseDown == DEACTIVATED)
		{
			this->mouseState = (this->mouseState == TRIGGER || this->mouseState == PRESS ? PRESS : TRIGGER);
		}
		else // INACTIVE
		{
			if (this->mouseState == TRIGGER || this->mouseState == PRESS)
			{
				this->mouseState = RELEASE;
			}
			else if (this->mouseState == RELEASE)
			{
				this->mouseState = IDLE;
			}
		}
		if (this->mouseDown == DEACTIVATED)
		{
			this->mouseDown = INACTIVE;
		}
		// key input update
		foreach (april::Key, it, this->controlKeys)
		{
			if (this->keyDowns[*it] == ACTIVATED)
			{
				this->keyDowns[*it] = ACTIVE;
			}
			if (this->keyDowns[*it] == ACTIVE || this->keyDowns[*it] == DEACTIVATED)
			{
				this->keyStates[*it] = (this->keyStates[*it] == TRIGGER || this->keyStates[*it] == PRESS ? PRESS : TRIGGER);
			}
			else // INACTIVE
			{
				if (this->keyStates[*it] == TRIGGER || this->keyStates[*it] == PRESS)
				{
					this->keyStates[*it] = RELEASE;
				}
				else if (this->keyStates[*it] == RELEASE)
				{
					this->keyStates[*it] = IDLE;
				}
			}
			if (this->keyDowns[*it] == DEACTIVATED)
			{
				this->keyDowns[*it] = INACTIVE;
			}
		}
		// button input update
		foreach (april::Button, it, this->controlButtons)
		{
			if (this->buttonDowns[*it] == ACTIVATED)
			{
				this->buttonDowns[*it] = ACTIVE;
			}
			if (this->buttonDowns[*it] == ACTIVE || this->buttonDowns[*it] == DEACTIVATED)
			{
				this->buttonStates[*it] = (this->buttonStates[*it] == TRIGGER || this->buttonStates[*it] == PRESS ? PRESS : TRIGGER);
			}
			else // INACTIVE
			{
				if (this->buttonStates[*it] == TRIGGER || this->buttonStates[*it] == PRESS)
				{
					this->buttonStates[*it] = RELEASE;
				}
				else if (this->buttonStates[*it] == RELEASE)
				{
					this->buttonStates[*it] = IDLE;
				}
			}
			if (this->buttonDowns[*it] == DEACTIVATED)
			{
				this->buttonDowns[*it] = INACTIVE;
			}
		}
	}
		
	void Input::reset()
	{
		this->mouseDown = INACTIVE;
		this->mouseState = IDLE;
		for_iter (i, 0, REACTOR_INPUT_MAX_KEYS)
		{
			this->keyDowns[i] = INACTIVE;
			this->keyStates[i] = IDLE;
			this->buttonDowns[i] = INACTIVE;
			this->buttonStates[i] = IDLE;
		}
		this->resetState();
	}

	/****************************************************************************************
	 * Mouse States
	 ****************************************************************************************/
		
	bool Input::isMouseTriggered()
	{
		return (this->mouseState == TRIGGER);
	}
		
	bool Input::isMouseTriggered(april::Key keyCode)
	{
		return (this->mouseState == TRIGGER && this->keyStates[keyCode] == TRIGGER);
	}
		
	bool Input::isMousePressed()
	{
		return (this->mouseState == TRIGGER || this->mouseState == PRESS);
	}
		
	bool Input::isMousePressed(april::Key keyCode)
	{
		return ((this->mouseState == TRIGGER && this->keyStates[keyCode] == TRIGGER) ||
			(this->mouseState == PRESS && this->keyStates[keyCode] == PRESS));
	}
		
	bool Input::isMouseReleased()
	{
		return (this->mouseState == RELEASE);
	}
		
	bool Input::isMouseReleased(april::Key keyCode)
	{
		return (this->mouseState == RELEASE && this->keyStates[keyCode] == RELEASE);
	}
		
	/****************************************************************************************
	 * Keyboard States
	 ****************************************************************************************/
		
	bool Input::isKeyTriggered(april::Key keyCode)
	{
		return (this->keyStates[keyCode] == TRIGGER);
	}
		
	bool Input::isKeyPressed(april::Key keyCode)
	{
		return (this->keyStates[keyCode] == TRIGGER || this->keyStates[keyCode] == PRESS);
	}
		
	bool Input::isKeyReleased(april::Key keyCode)
	{
		return (this->keyStates[keyCode] == RELEASE);
	}
		
	bool Input::isButtonTriggered(april::Button buttonCode)
	{
		return (this->buttonStates[buttonCode] == TRIGGER);
	}
		
	bool Input::isButtonPressed(april::Button buttonCode)
	{
		return (this->buttonStates[buttonCode] == TRIGGER || this->buttonStates[buttonCode] == PRESS);
	}
		
	bool Input::isButtonReleased(april::Button buttonCode)
	{
		return (this->buttonStates[buttonCode] == RELEASE);
	}
		
	/****************************************************************************************
	 * Context States
	 ****************************************************************************************/
		
	void Input::addState(chstr newContext)
	{
		this->stateStack += newContext;
	}
		
	hstr Input::removeState()
	{
		hstr result = REACTOR_INPUT_STATE_DEFAULT;
		if (this->stateStack.size() > 0)
		{
			result = this->stateStack.remove_last();
		}
		return result;
	}
		
	hstr Input::getCurrentState()
	{
		return (this->stateStack.size() == 0 ? REACTOR_INPUT_STATE_DEFAULT : this->stateStack.last());
	}
		
	void Input::resetState()
	{
		this->stateStack.clear();
	}
		
	/****************************************************************************************
	 * Methods
	 ****************************************************************************************/
		
	void Input::addKey(april::Key keyCode)
	{
		this->controlKeys |= keyCode;
	}
		
	void Input::addButton(april::Button buttonCode)
	{
		this->controlButtons |= buttonCode;
	}
		
	/****************************************************************************************
	 * Static Callbacks
	 ****************************************************************************************/
		
	void Input::onMouseDown(april::Key keyCode)
	{
		this->mouseDown = ACTIVATED;
		this->keyDowns[keyCode] = ACTIVATED;
	}
		
	void Input::onMouseUp(april::Key keyCode)
	{
		this->mouseDown = (this->mouseDown == ACTIVATED ? DEACTIVATED : INACTIVE);
		this->keyDowns[keyCode] = (this->keyDowns[keyCode] == ACTIVATED ? DEACTIVATED : INACTIVE);
	}
		
	void Input::onMouseCancel(april::Key keyCode)
	{
		this->mouseDown = INACTIVE;
		this->keyDowns[keyCode] = INACTIVE;
	}
		
	void Input::onMouseMove()
	{
	}
		
	void Input::onMouseScroll(float x, float y)
	{
	}
		
	void Input::onKeyDown(april::Key keyCode)
	{
		this->keyDowns[keyCode] = ACTIVATED;
	}
		
	void Input::onKeyUp(april::Key keyCode)
	{
		this->keyDowns[keyCode] = (this->keyDowns[keyCode] == ACTIVATED ? DEACTIVATED : INACTIVE);
	}
		
	void Input::onChar(unsigned int charCode)
	{
	}
		
	void Input::onTouch(const harray<gvec2>& touches)
	{
	}
		
	void Input::onButtonDown(april::Button buttonCode)
	{
		this->buttonDowns[buttonCode] = ACTIVATED;
	}
		
	void Input::onButtonUp(april::Button buttonCode)
	{
		this->buttonDowns[buttonCode] = (this->buttonDowns[buttonCode] == ACTIVATED ? DEACTIVATED : INACTIVE);
	}

}
