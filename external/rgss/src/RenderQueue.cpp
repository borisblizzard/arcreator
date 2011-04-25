#include <hltypes/harray.h>

#include "CodeSnippets.h"
#include "Renderable.h"
#include "RenderQueue.h"

namespace rgss
{
	RenderQueue::RenderQueue() : needsSorting(false)
	{
	}

	RenderQueue::~RenderQueue()
	{
		while (this->renderables.size() > 0)
		{
			this->renderables[0]->dispose();
		}
	}

	bool compareFunction(Renderable* a, Renderable* b)
	{
		return (a->getZ() < b->getZ() || a->getZ() == b->getZ() && a->getCounterId() < b->getCounterId());
	}

	void RenderQueue::draw()
	{
		if (this->needsSorting)
		{
			this->renderables.sort(&compareFunction);
			this->needsSorting = false;
		}
		foreach (Renderable*, it, this->renderables)
		{
			(*it)->draw();
		}
	}

	void RenderQueue::add(Renderable* renderable)
	{
		for_iter (i, 0, this->renderables.size())
		{
			if (renderable->getZ() < this->renderables[i]->getZ() ||
				renderable->getZ() == this->renderables[i]->getZ() &&
				renderable->getCounterId() == this->renderables[i]->getCounterId())
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
		this->needsSorting = true;
	}

}
