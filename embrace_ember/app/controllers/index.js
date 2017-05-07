import Ember from 'ember';
import moment from 'moment';

const { Controller, computed, get, getProperties, set } = Ember;

export default Controller.extend({
  latitude: "45.336702",
  longitude: "9.755859",
  app_id: "test",
  latLngValidations: [{
    message: 'Value is not a float.',
    validate: (value) => { return parseFloat(value) }
  }],
  dateValidations: [{
    message: 'Date is not parseable. Try an ISO-8601 string.',
    validate: (value) => { return new Date(value); }
  }],
  downloaded_at: computed('downloaded', {
    get() {
      return new Date(get(this, 'downloaded'));
    }
  }),
  downloaded: moment.utc().toISOString(),
  actions: {
    addMetric() {
      let { latitude, longitude, app_id, downloaded_at } = getProperties(this,
        'latitude', 'longitude', 'app_id', 'downloaded_at'
      );
      let metric = get(this, 'store').createRecord('download_metric', {
        app_id,
        downloaded_at,
        coordinates: {
          type: "Point",
          coordinates: [parseFloat(longitude), parseFloat(latitude)]
        }
      });
      set(this, 'errors', []);
      metric.save().then(() => {}, (error) => {
        set(this, 'errors', get(error, 'errors'));
      });
    },
    clickMap(event) {
      let { lat, lng } = get(event, 'latlng');
      set(this, 'latitude', lat);
      set(this, 'longitude', lng);
    }
  }
});
