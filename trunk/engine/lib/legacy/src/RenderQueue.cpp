#include <ruby.h>

#include <hltypes/harray.h>

#include "CodeSnippets.h"
#include "Renderable.h"
#include "RenderQueue.h"
#include "legacy.h"

namespace legacy
{
	RenderQueue::RenderQueue() : needsSorting(false)
	{
	}

	RenderQueue::~RenderQueue()
	{
		this->_updateCollections();
		harray<Renderable*> collections = this->collections;
		foreach (Renderable*, it, collections)
		{
			(*it)->dispose();
		}
		this->_updateRenderables();
		harray<Renderable*> renderables = this->renderables;
		foreach (Renderable*, it, renderables)
		{
			(*it)->dispose();
		}
	}

	bool _compareFunction(Renderable* a, Renderable* b)
	{
		return (a->getZ() < b->getZ() || a->getZ() == b->getZ() && a->getCounterId() < b->getCounterId());
	}

	void RenderQueue::_updateCollections()
	{
		if (this->addedCollections.size() > 0)
		{
			this->collections += this->addedCollections;
			this->addedCollections.clear();
		}
		if (this->removedCollections.size() > 0)
		{
			this->collections -= this->removedCollections;
			this->removedCollections.clear();
		}
	}

	void RenderQueue::_updateRenderables()
	{
		if (this->addedRenderables.size() > 0)
		{
			this->renderables += this->addedRenderables;
			this->addedRenderables.clear();
			this->needsSorting = true;
		}
		if (this->removedRenderables.size() > 0)
		{
			this->renderables -= this->removedRenderables;
			this->removedRenderables.clear();
		}
		if (this->needsSorting)
		{
			this->renderables.sort(&_compareFunction);
			this->needsSorting = false;
		}
	}

	void RenderQueue::draw()
	{
		this->_updateCollections();
		foreach (Renderable*, it, this->collections)
		{
			(*it)->update();
		}
		this->_updateRenderables();
		foreach (Renderable*, it, this->renderables)
		{
			(*it)->draw();
		}
	}

	void RenderQueue::add(Renderable* renderable)
	{
		// this part here is actually a dirty hack to separate tilemaps from normal renderable
		// objects, but it makes the high level code simpler and a lot more consistent
		if (renderable->isCollection())
		{
			this->addedCollections += renderable;
			return;
		}
		// adding the renderable into the queue
		this->addedRenderables += renderable;
	}

	void RenderQueue::remove(Renderable* renderable)
	{
		// this part here is actually a dirty hack to separate tilemaps from normal renderable
		// objects, but it makes the high level code simpler and a lot more consistent
		if (renderable->isCollection())
		{
			this->removedCollections += renderable;
			return;
		}
		// removing the renderable from the queue
		this->removedRenderables += renderable;
	}

	void RenderQueue::reorder(Renderable* renderable)
	{
		this->needsSorting = true;
	}

}
