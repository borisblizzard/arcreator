#include <april/Keys.h>
#include <aprilui/aprilui.h>
#include <hltypes/harray.h>

#include "System/Constants.h"
#include "System/Context.h"
#include "System/Main.h"
#include "System/Utility.h"

namespace System
{
	Context* context = NULL;
	
	/****************************************************************************************
	 * Construct/Destruct
	 ****************************************************************************************/

	Context::Context() : mouse(IDLE)
	{
		for_iter (i, 0, MAX_KEYS)
		{
			this->controlKeys += i;
		}
		this->reset();
	}

	Context::~Context()
	{
	}

	/****************************************************************************************
	 * Properties
	 ****************************************************************************************/

	Context::State Context::getState()
	{
		return (this->states.size() == 0 ? Context::DEFAULT : this->states.back());
	}
	
	void Context::setState(Context::State value)
	{
		this->states += value;
	}
	
	/****************************************************************************************
	 * Update
	 ****************************************************************************************/
	
	void Context::update()
	{
		switch (this->mouse)
		{
		case TRIGGER:
			this->mouse = PRESS;
			break;
		case RELEASE:
			this->mouse = IDLE;
			break;
		}
		foreach (unsigned int, it, this->controlKeys)
		{
            if (this->keys[*it])
			{
                this->released[*it] = false;
                if (!this->pressed[*it])
				{
                    this->pressed[*it] = true;
                    this->triggered[*it] = true;
				}
                else
				{
                    this->triggered[*it] = false;
				}
			}
            else if (!this->released[*it])
			{
                this->triggered[*it] = false;
                if (this->pressed[*it])
				{
                    this->pressed[*it] = false;
                    this->released[*it] = true;
				}
			}
            else
			{
                this->released[*it] = false;
			}
		}
	}

	void Context::reset()
	{
		this->mouse = IDLE;
		for_iter (i, 0, MAX_KEYS)
		{
			this->triggered[i] = false;
			this->pressed[i] = false;
			this->released[i] = false;
			this->keys[i] = false;
		}
		this->states.clear();
	}

	void Context::onMouseDown(float x, float y, int button)
	{
		this->mouse = TRIGGER;
	}

	void Context::onMouseUp(float x, float y, int button)
	{
		this->mouse = RELEASE;
	}
	
	void Context::onMouseMove(float x, float y)
	{
	}
	
	void Context::onKeyDown(unsigned int keycode)
	{
		this->keys[keycode] = true;
	}

	void Context::onKeyUp(unsigned int keycode)
	{
		this->keys[keycode] = false;
	}
	
	/// @todo Implementation
	void Context::onChar(unsigned int charcode)
	{
	}
	
	/****************************************************************************************
	 * Mouse States
	 ****************************************************************************************/

	bool Context::isMouseTriggered()
	{
		return (this->mouse == TRIGGER);
	}

	bool Context::isMousePressed()
	{
		return (this->mouse == TRIGGER || this->mouse == PRESS);
	}

	bool Context::isMouseReleased()
	{
		return (this->mouse == RELEASE);
	}

	/****************************************************************************************
	 * Keyboard States
	 ****************************************************************************************/

	bool Context::isKeyTriggered(unsigned int keycode)
	{
		return this->triggered[keycode];
	}
	
	bool Context::isKeyPressed(unsigned int keycode)
	{
		return this->pressed[keycode];
	}
	
	bool Context::isKeyReleased(unsigned int keycode)
	{
		return this->released[keycode];
	}

	/****************************************************************************************
	 * Context States setters
	 ****************************************************************************************/

	void Context::setPrevious()
	{
		if (this->states.size() > 0)
		{
			this->states.pop_back();
		}
	}

}
