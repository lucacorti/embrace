import Ember from 'ember';
import Model from 'ember-data/model';
import attr from 'ember-data/attr';

const { computed, get } = Ember;

export default Model.extend({
  downloaded_at: attr('date'),
  app_id: attr('string'),
  coordinates: attr(),
  point: computed('coordinates', {
    get() {
      let coords = get(this, 'coordinates.coordinates');
      return [coords[1], coords[0]];
    }
  })
});
