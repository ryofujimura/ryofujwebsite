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

type Skill = {
	name: string
	featured: boolean
}

interface SkillWithWorks extends Skill {
	works: Work[]
}

type Work = {
	id: string
	title: string
	skills: Skill['name'][]
	link?: string
	github?: string
}
