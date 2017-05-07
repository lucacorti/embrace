import Ember from 'ember';
import JSONAPISerializer from 'ember-data/serializers/json-api';

const { String: { camelize, capitalize } } = Ember;

export default JSONAPISerializer.extend({
  payloadKeyFromModelName(modelName) {
    return capitalize(camelize(modelName));
  },
});
