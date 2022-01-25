module.exports = {
	content: ['./src/**/*.{html,svelte}'],
	theme: {
		extend: {
			screens: {
				'<sm': { max: '639px' },
				'<md': { max: '767px' },
				'<lg': { max: '1023px' },
				'<xl': { max: '1279px' },
				'<2xl': { max: '1535px' }
			}
		}
	},
	plugins: [],
}
