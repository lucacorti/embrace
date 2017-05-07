import Ember from 'ember';

const { Route, get, inject, set } = Ember;

export default Route.extend({
  ajax: inject.service(),
  model() {
    return get(this, 'store').query('download-metric', { page_size: 100 });
  },
  setupController(controller, model) {
    set(controller, 'metrics', model);
    get(this, 'ajax').request('/api/stats').then((stats) => {
      set(controller, 'stats', stats.data);
      set(controller, 'stats-error', null);
    }, () => {
      set(controller, 'stats', null);
      set(controller, 'stats-error', 'Error while trying to fetch stats');
    });
  }
});
