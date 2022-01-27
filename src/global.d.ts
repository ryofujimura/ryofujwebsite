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

type SkillName =
	'Python' |
	'Swift / SwiftUI' |
	'HTML / CSS' |
	'JavaScript' |
	'Git / GitHub' |
	'Japanese'

type Skill = {
	name: SkillName
	featured: boolean
}

interface SkillWithWorks extends Skill {
	works: Work[]
}

type Work = {
	id: string
	title: string
	skills: SkillName[]
	link?: string
	github?: string
}
