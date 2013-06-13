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

    Experiment.makeGetSet = function(prop, calc) {
      return {
        /*
            function to generate getters and setters for accessors
        */

        get: function() {
          var animals;
          animals = this.get("animals");
          if (animals.length > 0) {
            return calc(animals);
          } else {
            return this["_" + prop];
          }
        },
        set: function(key, value) {
          var _ref;
          if (((_ref = this.get("animals")) != null ? _ref.length : void 0) > 0) {
            throw new Error("has animals inside");
          } else {
            return this["_" + prop] = value;
          }
        }
      };
    };

    Experiment.accessor("median", Experiment.makeGetSet("median", d3.median));

    Experiment.accessor("max", Experiment.makeGetSet("max", d3.max));

    Experiment.accessor("mean", Experiment.makeGetSet("mean", d3.mean));

    Experiment.accessor("min", Experiment.makeGetSet("min", d3.min));

    Experiment.accessor("number", Experiment.makeGetSet("number", function(arr) {
      return arr.length;
    }));

    return Experiment;

  })(Batman.Object);

}).call(this);
