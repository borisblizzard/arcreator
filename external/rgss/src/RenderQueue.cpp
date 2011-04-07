#include <hltypes/harray.h>

#include "CodeSnippets.h"
#include "Renderable.h"
#include "RenderQueue.h"

namespace rgss
{
	RenderQueue::~RenderQueue()
	{
		while (this->renderables.size() > 0)
		{
			this->renderables[0]->dispose();
		}
	}

	void RenderQueue::draw()
	{
		foreach (Renderable*, it, this->renderables)
		{
			(*it)->draw();
		}
	}

	void RenderQueue::add(Renderable* renderable)
	{
		for_iter (i, 0, this->renderables.size())
		{
			if (renderable->getZ() < this->renderables[i]->getZ())
			{
				this->renderables.insert_at(i, renderable);
				return;
			}
		}
		this->renderables += renderable;
	}

	void RenderQueue::remove(Renderable* renderable)
	{
		this->renderables -= renderable;
	}

	void RenderQueue::update(Renderable* renderable)
	{
		this->remove(renderable);
		this->add(renderable);
	}

}
