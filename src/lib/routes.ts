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
		title: 'Submission success!',
		subtitle: 'Contact',
		path: '/contact/success'
	},
]

export const paths: Path[] = routes.map(({ path }) => path)

export default routes
