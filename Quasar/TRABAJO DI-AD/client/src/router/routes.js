const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('src/pages/Login.vue') }
    ]
  },
  {
    path: '/Login',
    component: () =>
      import('layouts/MainLayout.vue'),
    children: [{
      path: '',
      component: () =>
        import('src/pages/Login.vue')
    }]
  },
  {
    path: '/Register',
    component: () =>
      import('layouts/MainLayout.vue'),
    children: [{
      path: '',
      component: () =>
        import('src/pages/Register.vue')
    }]
  },
  {
    path: '/About',
    component: () =>
      import('layouts/MainLayout.vue'),
    children: [{
      path: '',
      component: () =>
        import('src/pages/About.vue')
    }]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
