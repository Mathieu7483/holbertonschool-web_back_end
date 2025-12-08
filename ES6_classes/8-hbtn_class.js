export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  get size() {
    return this._size;
  }

  set size(newSize) {
    this._size = newSize;
  }

  get location() {
    return this._location;
  }

  set location(newLocation) {
    this._location = newLocation;
  }

  [Symbol.toPrimitive](cast) {
    if (cast === 'number') {
      return this.size;
    }
    if (cast === 'string') {
      return this.location;
    }
    return null;
  }
}
