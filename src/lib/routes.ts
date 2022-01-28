import works from './works'

const workRoutes = works.map((work): Route => ({
	title: work.title,
	subtitle: 'Works',
	path: `/works/${ work.id }`,
}))

const routes: Route[] = [
	{
		title: 'Home',
		path: '/',
		featured: true,
	},
	{
		title: 'Skills',
		path: '/skills',
		featured: true,
	},
	{
		title: 'Works',
		path: '/works',
		featured: true,
	},
	{
		title: 'About',
		path: '/about',
		featured: true,
	},
	{
		title: 'Contact',
		path: '/contact',
		featured: true,
	},
	{
		title: 'Submitted!',
		subtitle: 'Contact',
		path: '/contact/success'
	},
	...workRoutes,
]

export const paths: Path[] = routes.map(({ path }) => path)

export default routes
