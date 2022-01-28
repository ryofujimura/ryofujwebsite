/// <reference types="@sveltejs/kit" />

type Route = {
	title: string
	subtitle?: string
	path: Path
	featured?: boolean
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
	level: number
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
