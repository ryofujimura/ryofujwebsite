import { writable } from 'svelte/store'
import { browser } from '$app/env'

export let tabs = writable<Path[]>(
	browser
		? (JSON.parse(localStorage.getItem('tabs')) || [])
		: []
)

export let activeFeaturedSkill = writable<string | null>(
	browser
		? localStorage.getItem('activeFeaturedSkill')
		: null
)

export function localStore(key: string, value: any): void {
	let newValue = typeof value === 'string'
		? value
		: JSON.stringify(value)

	if (browser) {
		window.localStorage.setItem(key, newValue)
	}
}
