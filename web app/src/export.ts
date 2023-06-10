import { writable } from 'svelte/store';

export const food = writable('');

export const formValues = writable({
    product: "",
    ingre: "",
    sweet: "",
    fat: "",
    seas: "",
    aller: "",
    pred: ""
  });