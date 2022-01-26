import { writable } from 'svelte/store'
import { browser } from '$app/env'

export let tabs = writable<Path[]>(
	browser
		? (JSON.parse(localStorage.getItem('tabs')) || [])
		: []
)

export function localStore(key, value): void {
	if (browser) {
		window.localStorage.setItem(key, JSON.stringify(value))
	}
}
