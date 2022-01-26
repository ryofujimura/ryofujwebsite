const routes: Route[] = [
	{ title: 'Home', path: '/' },
	{ title: 'Skills', path: '/skills' },
	{ title: 'Works', path: '/works' },
	{ title: 'About', path: '/about' },
	{ title: 'Contact', path: '/contact' },
]

export const paths: Path[] = routes.map(({ path }) => path)

export default routes
