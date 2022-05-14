const { Octokit } = require("@octokit/core");
const fs=require('fs')
const octokit = new Octokit({
	auth: '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'
})
async function get_issues(){
	var owner=['Homebrew', 'CleverRaven', 'laravel', 'istio', 'bitcoin', 'sourcegraph', 'ArduPilot', 'radareorg', 'openssl', 'numpy', 'chef', 'cdnjs', 'openlayers', 'TryGhost', 'elixir-lang', 'PowerShell', 'MetaMask', 'grpc', 'RPCS3', 'microsoft', 'spring-projects', 'curl', 'codecombat', 'MonoGame', 'eclipse-theia', 'sequelize', 'monicahq', 'kubernetes', 'darkreader', 'parse-community', 'jerryscript-project', 'cypress-io', 'chartjs', 'angular', 'codesandbox', 'swaywm', 'Jermolene', 'borgbackup', 'realm', 'aws', 'keystonejs', 'aws-amplify', 'notepad-plus-plus', 'palantir', 'BVLC', 'reduxjs', 'mitmproxy', 'prometheus-operator', 'pallets', 'jetstack', 'mawww', 'jupyter', 'qutebrowser', 'golang', 'karma-runner', 'directus', 'sebastianbergmann', 'KaTeX', 'cython', 'snipe', 'streamlink', 'JedWatson', 'antlr', 'Dogfalo', 'kanboard', 'apple', 'dogecoin', 'pypa', 'svaarala', 'thoughtbot', 'puma', 'guzzle', 'google', 'GoogleChrome', 'lra', 'ankitects', 'microsoft', 'emotion-js', 'yannickcr', 'summernote', 'python-telegram-bot', 'Shopify', 'hexojs', 'wekan', 'Chocobozzz', 'hakimel', 'openai', 'pytorch', 'outline', 'junit-team', 'aquynh', 'segmentio', 'Netflix', 'postcss', 'nwjs', 'socketio', 'kubernetes', 'novus', 'FaridSafi', 'powerline', 'hackmdio', 'elastic', 'koajs', 'mjmlio', 'feathersjs', 'nextauthjs', 'StreisandEffect', 'polybar', 'nopSolutions', 'pockethub', 'elm', 'Humanizr', 'nolimits4web', 'jquense', 'thephpleague', 'jasmine', 'tensorflow', 'snabbdom', 'vuejs-templates', 'koel', 'microsoft', 'davidhalter', 'petkaantonov', 'beautify-web', 'wren-lang', 'airbnb', 'standard', 'uber-go', 'transmission', 'jorgebucaran', 'StevenBlack', 'barryvdh', 'tree-sitter', 'josdejong', 'asdf-vm', 'Aircoookie', 'hugapi', 'TypeStrong', 'senchalabs', 'redisson', 'facebookresearch', 'PyMySQL', 'facebook', 'callstack', 'Requarks', 'SwiftGen', 'reactjs', 'shentao', 'dompdf', 'bitly', 'CanCanCommunity', 'Popmotion', 'jprichardson', 'jpuri', 'mobile-shell', 'chocolatey', 'containrrr', 'postcss', 'express-validator', 'spencermountain', 'JetBrains', 'allinurl', 'gregberge', 'robinhood', 'javan', 'coryhouse', 'go-chi', 'http-party', 'amsul', 'daltoniam', 'chriskiehl', 'bkeepers', 'spotify', 'jacomyal', 'sindresorhus', 'travis-ci', 'BetterErrors', 'ramsey', 'google', 'FLEXTool', 'matryer', 'slim-template', 'nicklockwood', 'lottie-react-native', 'jackmoore', 'Tonejs', 'MichalLytek', 'stefanpenner', 'arashpayan', 'twitchtv', 'redux-offline', 'jsfiddle', 'kelektiv', 'FriendsOfPHP', 'thomaspark', 'HeroTransitions', 'JanDeDobbeleer', 'mafintosh', 'bytedeco', 'junyanz']

	var repo=['homebrew-cask', 'Cataclysm-DDA', 'framework', 'istio', 'bitcoin', 'sourcegraph', 'ardupilot', 'radare2', 'openssl', 'numpy', 'chef', 'cdnjs', 'openlayers', 'Ghost', 'elixir', 'PowerShell', 'metamask-extension', 'grpc-java', 'rpcs3', 'react-native-windows', 'spring-boot', 'curl', 'codecombat', 'MonoGame', 'theia', 'sequelize', 'monica', 'ingress-nginx', 'darkreader', 'parse-server', 'jerryscript', 'cypress', 'Chart.js', 'material', 'codesandbox-client', 'sway', 'TiddlyWiki5', 'borg', 'realm-cocoa', 'aws-cli', 'keystone-classic', 'amplify-js', 'notepad-plus-plus', 'blueprint', 'caffe', 'redux', 'mitmproxy', 'prometheus-operator', 'flask', 'cert-manager', 'kakoune', 'notebook', 'qutebrowser', 'go', 'karma', 'directus', 'phpunit', 'KaTeX', 'cython', 'snipe-it', 'streamlink', 'react-select', 'antlr4', 'materialize', 'kanboard', 'swift-nio', 'dogecoin', 'pipenv', 'duktape', 'administrate', 'puma', 'guzzle', 'libphonenumber', 'workbox', 'mackup', 'anki', 'WinObjC', 'emotion', 'eslint-plugin-react', 'summernote', 'python-telegram-bot', 'sarama', 'hexo', 'wekan', 'PeerTube', 'reveal.js', 'gym', 'fairseq', 'outline', 'junit4', 'capstone', 'evergreen', 'eureka', 'postcss', 'nw.js', 'socket.io', 'kompose', 'nvd3', 'react-native-gifted-chat', 'powerline', 'codimd', 'elasticsearch-js', 'koa', 'mjml', 'feathers', 'next-auth', 'streisand', 'polybar', 'nopCommerce', 'PocketHub', 'compiler', 'Humanizer', 'swiper', 'react-big-calendar', 'oauth2-server', 'jasmine', 'serving', 'snabbdom', 'webpack', 'koel', 'CNTK', 'jedi', 'bluebird', 'js-beautify', 'wren', 'lottie-android', 'standard', 'zap', 'transmission', 'hyperapp', 'hosts', 'laravel-ide-helper', 'tree-sitter', 'jsoneditor', 'asdf', 'WLED', 'hug', 'ts-node', 'connect', 'redisson', 'faiss', 'PyMySQL', 'fresco', 'linaria', 'wiki', 'SwiftGen', 'react-modal', 'vue-multiselect', 'dompdf', 'oauth2_proxy', 'cancancan', 'popmotion', 'node-fs-extra', 'react-draft-wysiwyg', 'mosh', 'choco', 'watchtower', 'autoprefixer', 'express-validator', 'compromise', 'ideavim', 'goaccess', 'loadable-components', 'faust', 'whenever', 'react-slingshot', 'chi', 'http-server', 'pickadate.js', 'Starscream', 'Gooey', 'dotenv', 'annoy', 'sigma.js', 'np', 'travis-ci', 'better_errors', 'uuid', 'sentencepiece', 'FLEX', 'xbar', 'slim', 'SwiftFormat', 'lottie-react-native', 'colorbox', 'Tone.js', 'type-graphql', 'es6-promise', 'appirater', 'twirp', 'redux-offline', 'togetherjs', 'node.bcrypt.js', 'Goutte', 'flexboxfroggy', 'Hero', 'oh-my-posh2', 'peerflix', 'javacv', 'pytorch-CycleGAN-and-pix2pix']

	for (var i=0;i<1;i++){
//		let {Alldata}=[]
		var j=2;
		let {index_data}=[]
		let {data}=await octokit.request('GET /repos/{owner}/{repo}/issues',{
			owner: owner[i],
			repo: repo[i],
			state: "all",
			per_page: 100,
			page: 1
		})
		var j=0;
		while(data[j]!=null){
			delete data[j].url;
			delete data[j].html_url;
			delete data[j].id;
			delete data[j].node_id;
			delete data[j].user.id;
			delete data[j].user.node_id;
			delete data[j].user.avatar_url;
			delete data[j].user.gravatar_id;
			delete data[j].user.followers_url;
			delete data[j].user.following_url;
			delete data[j].user.gists_url;
			delete data[j].user.starred_url;
			delete data[j].user.subscriptions_url;
			delete data[j].user.organizations_url;
			delete data[j].user.repos_url;
			delete data[j].user.events_url;
			delete data[j].user.received_events_url;
			delete data[j].user.site_admin;
			delete data[j].reactions;
			delete data[j].performed_via_github_app;
			j++;
		}
		data=JSON.stringify(data,undefined,4);
		var writerStream=fs.createWriteStream('./jsondata_comments/github_repo'+i+'.json');
		writerStream.write(data,'UTF-8');
		while(data!=null){
			j++;
			data = await octokit.request('GET /repos/{owner}/{repo}/issues/comments',{
				owner: owner[i],
				repo: repo[i],
				state: "all",
				per_page: 100,
				page: j
			})
			var j=0;
			while(data[j]!=null){
				delete data[j].url;
				delete data[j].html_url;
				delete data[j].id;
				delete data[j].node_id;
				delete data[j].user.id;
				delete data[j].user.node_id;
				delete data[j].user.avatar_url;
				delete data[j].user.gravatar_id;
				delete data[j].user.followers_url;
				delete data[j].user.following_url;
				delete data[j].user.gists_url;
				delete data[j].user.starred_url;
				delete data[j].user.subscriptions_url;
				delete data[j].user.organizations_url;
				delete data[j].user.repos_url;
				delete data[j].user.events_url;
				delete data[j].user.received_enents_url;
				delete data[j].user.site_admin;
				delete data[j].reactions;
				delete data[j].performed_via_github_app;
				j++;
			}
			data=JSON.stringify(data,undefined,4);
			writerStream.write(data,'UTF-8');
		}
		console.log("运行到这里")
		writerStream.end();
		writerStream.on('finish',function(){
			console.log("写入成功")
		})
		writerStream.on('error',function(err){
			console.log(err.stack);
		})
		console.log("程序执行完毕")
	}
}
get_issues();
