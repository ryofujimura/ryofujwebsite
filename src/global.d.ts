/// <reference types="@sveltejs/kit" />

type Site = {
	title: string
	description: string
}

type Route = {
	title: string
	path: Path
}

type Path = string

type Work = {
	id: string
	title: string
}

type Skill = {
	name: string
}