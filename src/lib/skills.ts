import works from './works'

export const skills: Skill[] = [
	{
		name: 'Python',
		featured: true,
		level: 9,
	},
	{
		name: 'Swift / SwiftUI',
		featured: true,
		level: 9,
	},
	{
		name: 'HTML / CSS',
		featured: true,
		level: 2,
	},
	{
		name: 'JavaScript',
		featured: true,
		level: 1,
	},
	{
		name: 'Git / GitHub',
		featured: false,
		level: 1,
	},
	{
		name: 'Japanese',
		featured: false,
		level: 10,
	},
]

export const skillsWithWorks: SkillWithWorks[] = skills.map(skill => ({
	...skill,
	works: works.filter(work => work.skills.includes(skill.name)),
}))
