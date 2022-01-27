import works from './works'

export const skills: Skill[] = [
	{
		name: 'Python',
		featured: true,
	},
	{
		name: 'Swift / SwiftUI',
		featured: true,
	},
	{
		name: 'HTML/CSS',
		featured: true,
	},
	{
		name: 'JavaScript',
		featured: true,
	},
	{
		name: 'Git / GitHub',
		featured: false,
	},
	{
		name: 'Japanese',
		featured: false,
	},
]

export const skillsWithWorks: SkillWithWorks[] = skills.map(skill => ({
	...skill,
	works: works.filter(work => work.skills.includes(skill.name)),
}))
