module.exports = function(grunt) {

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    useminPrepare: {
      html: 'src/index.html',
      options: {
        dest: 'dist'
      }
    },

    usemin: {
      html: 'dist/index.html'
    },

    copy: {
      fonts: {
        expand: true,
        cwd: 'src/font',
        src: '**',
        dest: 'dist/font'
      },
      index: {
        src: 'src/index.html',
        dest: 'dist/index.html'
      }
    },

    concat: {
      dist: {
        src: [
          'bower_components/jquery/**/*.min.js',
          'bower_components/angular/**/*.min.js',
          'bower_components/**/*.min.js',
          'src/lib/**/*.js',
          'src/js/**/*.js'
        ],
        dest: 'dist/build.js',
      }
    },

    uglify: {
      options: {
        mangle: {
          except: ['jQuery', 'angular']
        }
      },
      dist: {
        files: {
          'dist/build.min.js': ['dist/build.js']
        }
      }
    },

    cssmin: {
      combine: {
        files: {
          'dist/build.min.css': [
            'src/**/bootplus.min.css',
            'src/**/*.css'
          ]
        }
      }
    },

    imagemin: {
      options: {
        cache: false
      },

      dist: {
        files: [{
          expand: true,
          cwd: 'src/images',
          src: ['**/*.{png,jpg,gif}'],
          dest: 'dist/images'
        }]
      }
    },

    jshint: {
      files: ['Gruntfile.js', 'src/js/**/*.js', 'test/**/*.js'],
      options: {
        // options here to override JSHint defaults
        globals: {
          jQuery: true,
          console: true,
          module: true,
          document: true
        }
      }
    },

    htmlmin: {
      dist: {
        options: {
          removeComments: true,
          collapseWhitespace: true
        },
        files: {
          'dist/index.html': 'dist/index.html'
        }
      }
    },

    watch: {
      gruntfile: {
        files: 'Gruntfile.js',
        tasks: ['jshint'],
      },
      src: {
        files: ['bower_components/**/*.js', 'src/**/*.*'],
        tasks: ['default'],
      }
    }

  });

  // measures the time each task takes
  require('time-grunt')(grunt);

  grunt.loadNpmTasks('grunt-usemin');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-contrib-htmlmin');
  grunt.loadNpmTasks('grunt-contrib-imagemin');
  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-watch');

  grunt.registerTask('default', [
    'jshint',
    'copy',
    'useminPrepare',
    'concat',
    'cssmin',
    //'uglify',
    'imagemin',
    'usemin',
    'htmlmin'
  ]);
};
