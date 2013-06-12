// Generated by CoffeeScript 1.6.3
(function() {
  var __hasProp = {}.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

  Denigma.Experiment = (function(_super) {
    __extends(Experiment, _super);

    /*
      class that describes experimental group (it can be either test or control one
      it has many accessors as the info is often incomplete
    */


    Experiment.prototype._number = 0;

    Experiment.prototype._min = -1;

    Experiment.prototype._mean = 0;

    Experiment.prototype._median = 0;

    Experiment.prototype._max = 0;

    function Experiment(line, animals) {
      this.line = line;
      if (animals == null) {
        animals = [];
      }
      if ((animals != null)) {
        this.set("animals", animals);
      } else {
        this.set("animals", []);
      }
    }

    Experiment.prototype.rnd = function(numberToRound) {
      return Math.round(numberToRound * 100) / 100;
    };

    Experiment.accessor("median", {
      get: function() {
        return this._median;
      },
      set: function(value) {
        return this._median = value;
      }
    });

    Experiment.accessor("max", {
      get: function() {
        var animals, i, sum, _i, _len;
        animals = this.get("animals");
        if (animals.length > 0) {
          sum = 0;
          for (_i = 0, _len = animals.length; _i < _len; _i++) {
            i = animals[_i];
            if (i > sum) {
              sum = i;
            }
          }
          return sum;
        } else {
          return this._max;
        }
      },
      set: function(key, value) {
        var _ref;
        if (((_ref = this.get("animals")) != null ? _ref.length : void 0) > 0) {
          throw new Error("has animals inside");
        } else {
          return this._max = value;
        }
      }
    });

    Experiment.accessor("mean", {
      get: function() {
        var animals, i, sum, _i, _len;
        animals = this.get("animals");
        if (animals.length > 0) {
          sum = 0;
          for (_i = 0, _len = animals.length; _i < _len; _i++) {
            i = animals[_i];
            sum = sum + i;
          }
          return this.rnd(sum / animals.length);
        } else {
          return this._mean;
        }
      },
      set: function(key, value) {
        var _ref;
        if (((_ref = this.get("animals")) != null ? _ref.length : void 0) > 0) {
          throw new Error("has animals inside");
        } else {
          return this._mean = value;
        }
      }
    });

    Experiment.accessor("min", {
      get: function() {
        var animals, i, sum, _i, _len;
        animals = this.get("animals");
        if (animals.length > 0) {
          sum = 0;
          for (_i = 0, _len = animals.length; _i < _len; _i++) {
            i = animals[_i];
            if (i < sum || sum === 0) {
              sum = i;
            }
          }
          return sum;
        } else {
          return this._min;
        }
      },
      set: function(key, value) {
        var _ref;
        if (((_ref = this.get("animals")) != null ? _ref.length : void 0) > 0) {
          throw new Error("has animals inside");
        } else {
          return this._min = value;
        }
      }
    });

    Experiment.accessor("number", {
      get: function() {
        var animals;
        animals = this.get("animals");
        if (animals.length > 0) {
          return animals.length;
        } else {
          return this._number;
        }
      },
      set: function(key, value) {
        var _ref;
        if (((_ref = this.get("animals")) != null ? _ref.length : void 0) > 0) {
          throw new Error("has animals inside");
        } else {
          return this._number = value;
        }
      }
    });

    return Experiment;

  })(Batman.Object);

}).call(this);
