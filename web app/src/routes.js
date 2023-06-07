import home from './routes/+page.svelte';
import result from './routes/result/+page.svelte';

const routes = [
  {
    path: '/',
    component: home
  },
  {
    path: '/result',
    component: result
  }
];

export default routes;