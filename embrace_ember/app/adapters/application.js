import ENV from '../config/environment';
import Ember from 'ember';
import JSONAPIAdapter from 'ember-data/adapters/json-api';

const { computed, get } = Ember;

export default JSONAPIAdapter.extend({
  urlForFindAll(modelName, snapshot) {
    let url = this._super(...arguments);
    let params = this.queryParamsToString(modelName, get(snapshot, 'adapterOptions.query'));
    return `${url}/${params}`;
  },
  urlForFindRecord(id, modelName, snapshot) {
    let url = this._super(...arguments);
    let params = this.queryParamsToString(modelName, get(snapshot, 'adapterOptions.query'));
    return `${url}/${params}`;
  },
  urlForCreateRecord(modelName, snapshot) {
    let url = this._super(...arguments);
    let params = this.queryParamsToString(modelName, get(snapshot, 'adapterOptions.query'));
    return `${url}/${params}`;
  },
  urlForQuery(/* query, modelName*/) {
    let url = this._super(...arguments);
    return `${url}/`;
  },
  queryParamsToString(modelName, query) {
    if (!query) {
      return '';
    }
    return Object.keys(query).reject((item) => {
      return item === modelName;
    }).reduce((acc, item) => {
      let param = encodeURIComponent(item);
      let value = encodeURIComponent(query[item]);
      return `${acc}${param}=${value}&`;
    }, '?');
  },
  // host: computed({
  //   get() {
  //     return ENV.APP.API_HOST;
  //   }
  // }),
  namespace: computed({
    get() {
      return ENV.APP.API_NAMESPACE;
    }
  })
});
