#!/bin/sh


# Put tutorial library files into $PATH
PATH="$PWD/.lib:$PATH"

. shell-compat-test.sh


source help.sh $@ <<HELP
Git Tag Syntax

* Learn the basic command syntax and concepts for git tagging
* Add new tags to commits
* Remove tags from commits
* Manage tags on remote repositories

Commands used in this lesson
============================
* git clone
* git log
* git remote
* git tag
* git add
* git commit
* git push
HELP


_REPO_NAME=tags
_REPO_URL_SSH=git@gitlab.cs.usu.edu:erik.falor/$_REPO_NAME
_SUGGESTED_REMOTE_REPO_NAME=$_REPO_NAME

# Git commit ID given by `git rev-parse --short HEAD`
_REPO_STARTER_COMMIT=ff12f8b

# Git commit ID given by `git rev-parse HEAD`
_REPO_STARTER_COMMIT_L=ff12f8bfde57f525da46cb4edea55e5116d195d8

# Git commit ID given by `git rev-parse --short HEAD~`
_REPO_2ND_COMMIT=faf9d69

# Git commit ID given by `git rev-parse HEAD~`
_REPO_2ND_COMMIT_L=faf9d695e7d1c3ac9c9b4023ce862736ede431f8


source ansi-terminal-ctl.sh
DuckieCorp()   { echo ${_Y}DuckieCorp${_z} ; }
_local()       { (( $# == 0 )) && echo $(ylw local)        || echo $(ylw $*); }
_remote()      { (( $# == 0 )) && echo $(mgn remote)       || echo $(mgn $*); }
_origin()      { (( $# == 0 )) && echo $(red origin)       || echo $(red $*); }
_md()          { (( $# == 0 )) && echo $(blu MARKDOWN)     || echo $(blu $*) ; }


source record.sh
if [[ -n $_TUTR ]]; then
	source generic-error.sh
	source git.sh
	source nonce.sh
	source open.sh
fi

repo_warning() {
	cat <<-MSG
	${_Y}        .         ${_Z}
	${_Y}       / \        ${_Z} The repository $(path ../../$_REPO_NAME) already exists.
	${_Y}      / _ \       ${_Z} This lesson requires you to re-clone this
	${_Y}     / | | \      ${_Z} repository to begin from scratch.
	${_Y}    /  | |  \     ${_Z}
	${_Y}   /   |_|   \    ${_Z} To proceed, you may delete that existing
	${_Y}  /     _     \   ${_Z} repository with $(cmd "rm -rf ../../$_REPO_NAME"),
	${_Y} /     (_)     \  ${_Z} or rename it with the $(cmd mv) command.
	${_Y}/_______________\ ${_Z}

	This repository will also be present on your Gitlab account.
	Later in this lesson you will be asked to choose a name for this
	$(_remote) repository.  Choose something unique to avoid a clash.
	MSG
}

warn_not_in_repo() {
	cat <<-MSG
	This step $(bld must) be completed inside the repository directory.
	You will be unable to complete this step outside of the repository.
	MSG
}

must_be_in_repo() {
	if [[ "$PWD" != "$_REPO_PATH" ]]; then
		_tutr_warn warn_not_in_repo
	fi
}

# Open the current Git repo's 1st remote web page (if present)
browse_to_repo() {
	_tutr_git_repo_https_url
	_tutr_open $REPLY || _tutr_warn echo "Open '$REPLY' in your web browser"
}

setup() {
	_tutr_record_repeat_prompt
	source screen-size.sh 80 30
	export _ORIG_PWD="$PWD"
	export _GPARENT="$(cd ../.. && pwd)"
	export _REPO_PATH="$_GPARENT/$_REPO_NAME"
	# Check if repo for lesson already exists
	if [[ -d "$_REPO_PATH/.git" ]]; then
		_tutr_err repo_warning
		return 1
	fi
}


prologue() {
	[[ -z $DEBUG ]] && clear
	cat <<-PROLOGUE
	Git Tag Syntax

	In this lesson you will learn how to

	* Use the basic command syntax and concepts for git tagging
	* Add new tags to commits
	* Remove tags from commits
	* Manage tags on $(_remote) repositories

	Commands used in this lesson
	============================
	* git clone
	* git log
	* git remote
	* git tag
	* git add
	* git commit
	* git push

	PROLOGUE

	_tutr_pressanykey

	cat <<-PROLOGUE

	$(ylw "Note that an internet connection is required for this lesson.")

	$(ylw "If you aren't online now, restart this lesson when you are.")

	PROLOGUE

	_tutr_pressanykey

	cat <<-TAGEXPLAIN

	As your projects grow larger, it becomes more and more challenging to
	keep track of important commits.  The difficulty arises from the awkward
	commit IDs Git forces us to look at:

	  $(ylw_ dbd7d3473fca1b0f7c7c0dfd271451f78902ddc9)

	A 'tag' in Git is a human-friendly "nickname" for commits.

	Like a commit ID, a tag can locate a particular commit.  One might do
	this, for example, to mark an important milestone in a project's
	life.

	Not all commits deserve to be tagged.  At $(DuckieCorp) you will use tags
	on commits that mark the fulfillment of the stages of the Software
	Development Plan.

	This lesson prepares you to use Git tags in your assignments.

	TAGEXPLAIN

	_tutr_pressanykey
}


cd_dotdot_rw() {
	cd "$_ORIG_PWD"
}

cd_dotdot_ff() {
	cd "$_GPARENT"
}

cd_dotdot_prologue() {
	cat <<-MSG
	In this lesson you will clone a small repository to play around in.

	Before you clone it down, $(cmd cd) up two directories to avoid putting the
	new repository inside your assignment repo.
	MSG
}

cd_dotdot_test() {
	if _tutr_nonce; then return $PASS
	elif [[ "$PWD" != "$_GPARENT" ]]; then return $WRONG_PWD
	else return 0
	fi
}

cd_dotdot_hint() {
	_tutr_generic_hint $1 cd "$_GPARENT"
}



clone_repository_rw() {
	rm -rf "$_REPO_PATH"
}

clone_repository_ff() {
	git clone $_REPO_URL_SSH
}

clone_repository_pre() {
	if [[ -d "$_REPO_PATH/.git" ]]; then
		_tutr_err repo_warning
		return 1
	fi
}

clone_repository_prologue() {
	cat <<-MSG
	Now that you're here, clone the repository at

	  $(path $_REPO_URL_SSH)
	MSG
}

clone_repository_test() {
	HTTPS_URL=99
	if   _tutr_nonce rm; then return $PASS
	elif [[ ${_CMD[0]} = git && ${_CMD[1]} = clone && ${_CMD[2]} = http* ]]; then return $HTTPS_URL
	elif [[ -d "$_REPO_PATH/.git" ]]; then return 0
	else _tutr_generic_test -c git -a clone -a "^($_REPO_URL_SSH(.git)?)$" -d "$_GPARENT"
	fi
}

clone_repository_hint() {
	case $1 in
		$PASS)
			;;

		$STATUS_FAIL)
			cat <<-MSG
			'git clone' failed unexpectedly.

			If the above error message includes the phrases "fatal: unable to
			access" and "Connection refused", that indicates an issue with your
			network connection.  Ensure that you are connected to the internet and
			try again.

			If the error persists or is different, please contact
			erik.falor@usu.edu for help.
			Copy the full command and all of its output.

			MSG
			;;

		$WRONG_PWD)
			_tutr_generic_hint $1 git "$_GPARENT"
			;;

		$HTTPS_URL)
			cat <<-MSG
			You cloned the repository with an HTTPS URL.  In this class you
			should always use SSH URLs with Git.

			Remove the repo you just cloned:
			  $(cmd rm -rf $_REPO_NAME)

			Then re-clone it by running:
			  $(cmd git clone $_REPO_URL_SSH)

			If you do not have an SSH key set up, reach out to
			erik.falor@usu.edu for help.
			MSG
			;;

		*)
			_tutr_generic_hint $1 git

			cat <<-MSG

			Clone the demo repo by running
			  $(cmd git clone $_REPO_URL_SSH)
			MSG
			;;
	esac
}

clone_repository_epilogue() {
	cat <<-:
	FYI, the repository that you just cloned will be automatically erased
	from your computer at the end of this tutorial.

	:
	_tutr_pressanykey
}



cd_into_repo_rw() {
	cd "$_GPARENT"
}

cd_into_repo_ff() {
	cd "$_REPO_PATH"
}

cd_into_repo_prologue() {
	cat <<-MSG
	Enter the directory $(path $_REPO_NAME)
	MSG
}

cd_into_repo_test() {
	if   [[ "$PWD" == "$_REPO_PATH" ]]; then return 0
	elif _tutr_nonce; then return $PASS
	else return $WRONG_PWD
	fi
}

cd_into_repo_hint() {
	[[ $1 == $PASS ]] && return
	_tutr_minimal_chdir_hint "$_REPO_PATH"
}

cd_into_repo_post() {
	## What is this for?
	if [[ $_RES -ne 0 ]]; then
		_tutr_die printf "'Then send it to erik.falor@usu.edu.'"
	fi

	_ORIG_URL=$(git remote get-url origin)
}



ls_inspect_repo_pre() {
	must_be_in_repo
}

ls_inspect_repo_prologue() {
	cat <<-MSG
	Take a look at the files here with $(cmd ls)
	MSG
}

ls_inspect_repo_test() {
	_tutr_generic_test -c ls -x -d "$_REPO_PATH"
}

ls_inspect_repo_hint() {
	_tutr_generic_hint $1 ls "$_REPO_PATH"
}

ls_inspect_repo_epilogue() {
	_tutr_pressanykey
}


inspect_repo_prologue() {
	cat <<-MSG
	Yeah, it's not too fancy in here.

	Run $(cmd git log) to review the commit history.
	MSG
}

inspect_repo_test() {
	if _tutr_nonce; then
		return $PASS
	else
		_tutr_generic_test -c git -a log -d "$_REPO_PATH"
	fi
}

inspect_repo_hint() {
	_tutr_generic_hint $1 git "$_REPO_PATH"

	cat <<-MSG

	Review the commit history with $(cmd git log).
	MSG
}


inspect_repo_epilogue() {
	_tutr_pressanykey

	cat <<-MSG

	This output tells you that this repository has 3 commits.  The most
	recent commit is at the top, with older commits following in order to
	the oldest.

	Here's what the first block of output means:

	$(ylw_ commit $_REPO_STARTER_COMMIT)
	  the SHA-1 fingerprint of this commit

	$(cyn "HEAD ->") $(grn master)
	  the currently checked-out commit ($(cyn HEAD)) is the tip of a branch
	  named ($(grn master))

	$(ylw tag: final)
	  this commit is tagged with the name $(ylw final)

	$(_remote origin/master)$(ylw_ ,) $(_remote origin/HEAD)
	  indicates this commit is also the tip of the $(grn master) branch on
	  the $(_remote) server, and that this commit is what's currently checked-out
	  there

	MSG

	_tutr_pressanykey

	cat <<-MSG

	Pay close attention to the $(ylw tag: final) marker on the latest commit.
	This will come into play later in this lesson.

	MSG
	_tutr_pressanykey
}


remote_rename_rw() {
	for REMOTE in $(git remote); do
		git remote remove $REMOTE
	done
	git remote add origin $_REPO_URL_SSH
}

remote_rename_ff() {
	git remote rename origin old-origin
}

remote_rename_prologue() {
	cat <<-MSG
	Tags are going to become an important part of your workflow in
	assignments going forward.  In this lesson you will practice creating
	them and pushing them to my GitLab server.  You need to change this
	repository's $(_remote) URL to point to your account on GitLab.

	Just like previous assignments, the first step is to rename the $(_origin)
	$(_remote) to $(_remote old-origin).

	As a reminder, the command looks like this:
	  $(cmd git remote rename '<old>' '<new>')

	Replace $(cmd '<old>') and $(cmd '<new>') as appropriate.
	MSG
}


remote_rename_hint() {
	if [[ $1 == $PASS ]]; then return; fi

	_tutr_generic_hint $1 git "$_REPO_PATH"

	cat <<-MSG

	If you want to see the $(_remote) repositories and their URLs, run:
	  $(cmd git remote -v)

	To rename $(_origin) to $(_origin old-origin), run:
	  $(cmd git remote rename origin old-origin)
	MSG
}

remote_rename_test() {
	if _tutr_nonce; then return $PASS
	elif [[ $PWD != $_REPO_PATH ]]; then return $WRONG_PWD
	elif [[ ${_CMD[0]} = git && ${_CMD[1]} = help ]]; then return $PASS
	elif [[ ${_CMD[0]} = git && ${_CMD[1]} = status ]]; then return $PASS
	elif [[ ${_CMD[0]} = git && ${_CMD[1]} = log ]]; then return $PASS
	elif [[ ${_CMD[0]} = git && ${_CMD[1]} = remote && ${_CMD[2]} = -v ]]; then return $PASS
	else
		if   git remote | command grep -q -E '^old-origin$'; then return 0
		elif [[ $( git remote | wc -l ) = 0 ]] ; then return 0
		else _tutr_generic_test -c git -a remote -a rename -a origin -a old-origin -d "$_REPO"
		fi
	fi
}

remote_rename_post() {
	# Enable us to adjust prose if origin gets removed instead of renamed
	if [[ $(git remote | wc -l) = 0 ]]; then
		_REMOVED_ORIGIN=yep
	else
		_REMOVED_ORIGIN=nope
	fi
}

remote_rename_epilogue() {
	if [[ $_REMOVED_ORIGIN = yep ]]; then
		echo "Well, that was ONE way to do it."
	else
		echo "Perfect!"
	fi

	cat <<-MSG

	The reason I asked you to rename $(_origin) instead of just deleting it
	is so that your repository will always remember where it came from.
	This way, if I ever need to fix a bug in the starter code, you can
	easily incorporate it into your repository.

	It is not really necessary right now, but it's a good habit to follow.

	MSG

	if [[ $_REMOVED_ORIGIN = yep ]]; then
		cat <<-MSG
		I see that you removed $(_origin).  Don't do that on a real assignment.
		Because it's not critical to this lesson, we'll just continue on.

		MSG
	fi
	_tutr_pressanykey
}



remote_add_rw() {
	git remote remove origin
}

remote_add_ff() {
	_tutr_info printf "'Just guessing... using /tmp/tags as the remote URL for origin'"
	if [[ ! -d /tmp/tags ]]; then
		git clone --bare $_REPO_PATH /tmp/tags
	fi
	git remote add origin /tmp/tags
}

remote_add_pre() {
	must_be_in_repo
}

remote_add_prologue() {
	cat <<-MSG
	Now you can add a new $(_origin) URL.  I'm not going to be very strict
	about the URL you use, so long as it is linked to $(wht your) account
	on GitLab.

	Construct the URL like this:

	  git@gitlab.cs.usu.edu:$(mgn "<your_gitlab_username>")/$(cyn "<repository_name>")

	Replace $(mgn "<your_gitlab_username>") with your GitLab username,
	i.e., the name you see in the address bar after you log on to GitLab.

	$(cyn "<repository_name>") should be descriptive, and something that won't
	clash with your assignment repositories.  Might I suggest $(wht "'$_SUGGESTED_REMOTE_REPO_NAME'")?

	If you've already used that name with another repository, just add a
	number to the end of it so that it is unique.

	The command to use is
	  $(cmd git remote add origin NEW_URL)
	MSG
}

remote_add_test() {
	NO_ORIGIN_URL=99
	URL_NOT_GITLAB=98
	URL_USER_IS_ERIK=97
	URL_IS_HTTPS_AMALGATION_OF_HTTPS_AND_SSH=96
	URL_IS_SSH_AMALGATION_OF_HTTPS_AND_SSH=95
	URL_SCHEME_WRONG=94

	if   [[ $PWD != $_REPO_PATH ]]; then return $WRONG_PWD
	elif _tutr_nonce; then return $PASS
	elif [[ ${_CMD[0]} = git && ${_CMD[1]} = help ]]; then return $PASS
	elif [[ ${_CMD[0]} = git && ${_CMD[1]} = status ]]; then return $PASS
	elif [[ ${_CMD[0]} = git && ${_CMD[1]} = log ]]; then return $PASS
	elif [[ ${_CMD[0]} = git && ${_CMD[1]} = remote && ${_CMD[2]} = -v ]]; then return $PASS
	elif [[ ${_CMD[0]} = git && ${_CMD[1]} = remote && ${_CMD[2]} = remove ]]; then return $PASS
	elif [[ ${_CMD[0]} = git && ${_CMD[1]} = remote && ${_CMD[2]} = rename ]]; then return $PASS
	elif [[ ${_CMD[0]} = git && ${_CMD[1]} != remote ]]; then return 95
	fi

	local URL=$(git remote get-url origin 2>/dev/null)
	if   [[ -z $URL ]]; then return $NO_ORIGIN_URL
	elif [[ $URL != *gitlab.cs.usu.edu* ]]; then return $URL_NOT_GITLAB
	elif [[ $URL = [/:]*erik.falor/* ]]; then return $URL_USER_IS_ERIK
	elif [[ $URL = https://gitlab.cs.usu.edu:* ]]; then return $URL_IS_HTTPS_AMALGATION_OF_HTTPS_AND_SSH
	elif [[ $URL = git@gitlab.cs.usu.edu/* ]]; then return $URL_IS_SSH_AMALGATION_OF_HTTPS_AND_SSH
	elif [[ $URL != https:* && $URL != git@* ]]; then return $URL_SCHEME_WRONG
	elif [[ $URL = https://gitlab.cs.usu.edu/*/* || $URL = git@gitlab.cs.usu.edu:*/* ]]; then return 0
	else _tutr_generic_test -c git -n -d "$_REPO_PATH"
	fi
}

remote_add_hint() {
	case $1 in
		$PASS)
			return
			;;

		$NO_ORIGIN_URL)
			cat <<-MSG
			There is no $(_remote) called $(_origin).  Create it with
			  $(cmd git remote add origin NEW_URL).

			Replace "NEW_URL" in the above command with an address as
			described above (run $(cmd tutor hint) to review the instructions).

			MSG
			;;

		$URL_NOT_GITLAB)
			cat <<-MSG
			The hostname of the URL should be 'gitlab.cs.usu.edu'.

			If you push your code to the wrong Git server it will not be submitted.

			Use $(cmd git remote remove origin) to erase this and try again.
			MSG
			;;

		$URL_USER_IS_ERIK)
			cat <<-MSG
			$(_origin) points to the address of MY repo, not YOURS! The 
			$(mgn "<gitlab_username>") portion of the URL is $(mgn erik.falor) when it should
			be replaced with $(bld your) username. 

			Use $(cmd git remote remove origin) to erase this and try again.
			MSG
			;;

		$URL_IS_HTTPS_AMALGATION_OF_HTTPS_AND_SSH)
			cat <<-MSG
			The HTTPS address you entered will not work because there is a colon ':'
			between the hostname 'gitlab.cs.usu.edu' and your username.  (Use $(cmd git)
			$(cmd remote -v) to see for yourself).

			Instead of a colon that character should be a front slash '/'.

			Use $(cmd git remote remove origin) to erase this and try again.
			MSG
			;;

		$URL_IS_SSH_AMALGATION_OF_HTTPS_AND_SSH)
			cat <<-:
			This SSH address will not work because there is a slash '/' between the
			hostname 'gitlab.cs.usu.edu' and your username.  (Use $(cmd git remote -v) to
			see for yourself).

			Instead of a slash that character should be a colon ':'

			Use $(cmd git remote remove origin) to erase this and try again.
			:
			;;

		$URL_SCHEME_WRONG)
			cat <<-MSG
			The URL must start with $(bld git@).  Otherwise, Git will be unable
			to talk to the server.

			Use $(cmd git remote remove origin) to erase this and try again.
			MSG
			;;
		*)
			_tutr_generic_hint $1 'git remote' "$_REPO_PATH"
			;;
	esac
	cat <<-MSG

	After you figure out what NEW_URL should be, use this command:
	  $(cmd git remote add origin NEW_URL)

	Use $(cmd tutor hint) to review the instructions about the new URL.
	MSG
}

remote_add_epilogue() {
	if [[ "$(git remote -v 2>/dev/null | command grep origin)" == *"https://"* ]]; then
		cat <<-MSG
		You set up your repository with an HTTPS URL.  This will work, but isn't
		ideal. Just a heads up, you will be asked for your GitLab credentials
		frequently during the lesson because of it.

		MSG
		_tutr_pressanykey
	fi
}



# There is no good way to rewind this action
# push_repo_rw() {}

push_repo_ff() {
	git push -u origin master
}

push_repo_prologue() {
	cat <<-MSG

	Now you can push to the new $(_origin).  Do this with
	  $(cmd git push -u origin master)

	The $(cmd -u) flag will save you keystrokes in the future.  It tells Git that
	$(_origin) is the default destination when you run a plain, old $(cmd git push).

	If you don't set this option now, you will need to type
	  $(cmd git push origin master)
	every time you need to push your work to $(_origin).

	What can I say?  We programmers are lazy.
	MSG
}

push_repo_test() {
	[[ "$PWD" != "$_REPO_PATH"* ]] && return $WRONG_PWD
	if   [[ ${_CMD[*]} == "git help push" ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git remote"* ]]; then return $PASS
	elif _tutr_nonce; then return $PASS
	fi
	_tutr_generic_test -c git -a push -a -u -a origin -a master
}

push_repo_hint() {
	case $1 in
		$PASS)
			return
			;;
		*)
			_tutr_generic_hint $1 git "$_REPO_PATH"
			;;
	esac

	cat <<-MSG
	Run $(cmd git push -u origin master) to proceed.

	If you are having trouble pushing to the $(_remote), inspect the output of
	$(cmd git remote -v) to check that the remote URL was set correctly.

	If you made a mistake, fix it with $(cmd git remote set-url origin NEW_URL)

	MSG
}

push_repo_epilogue() {
	cat <<-MSG

	${_Y}      _         ${_Z} Your repository is now on GitLab!
	${_Y}     /(|        ${_Z}
	${_Y}    (  :        ${_Z} I'm opening this repo's home page in your web
	${_Y}  ___\  \  _____${_Z} browser so you can see what it looks like.
	${_Y} (____)  \`|     ${_Z} Near the top of the page, just beneath this
	${_Y}(____)|   |     ${_Z} repo's name, you'll see:
	${_Y} (____).__|     ${_Z}
	${_Y}  (___)__.|_____${_Z} $(bld 3 Commits  1 Branch  0 Tags  113KB Project Storage)

	Pay close attention to $(bld 0 Tags).  $(bld git log) just said that there is a
	tag called $(ylw final).  But why isn't it on Gitlab?
	MSG

	browse_to_repo

	if [[ -n $REPLY ]]; then
		cat <<-MSG

		If a browser window didn't pop up for you, go to
		  $(cmd $REPLY)

		MSG
	fi

	_tutr_pressanykey
}



# There is no good way to rewind this action
# push_tag_1st_time_rw() {}

push_tag_1st_time_ff() {
	git push origin final
}

push_tag_1st_time_prologue() {
	cat <<-MSG
	By default, Git does not automatically push tags to $(_remote remotes).  This is
	because tags are most commonly used on one's $(_local) computer only.  When
	a programmer wants to share a tag with others, they have to be $(bld explicit).

	You can push tags to a $(_remote) by naming them on the command line, after
	the name of the $(_remote) destination:
	  $(cmd "git push origin TAG_NAME...")

	Now, push the $(ylw final) tag (the one on the most recent commit) to
	your $(_remote) repo $(_origin).
	MSG
}

push_tag_1st_time_test() {
	[[ "$PWD" != "$_REPO_PATH"* ]] && return $WRONG_PWD
	if _tutr_nonce; then
		return $PASS
	elif [[ ${_CMD[*]} == *"--tags" ]]; then
		if (( ${#_CMD[@]} == 3 )); then
			_tutr_generic_test -c git -a push -a "--tags"
		else
			_tutr_generic_test -c git -a push -a origin -a "--tags"
		fi
	else
		_tutr_generic_test -c git -a push -a origin -a final -d "$_REPO_PATH"
	fi
}

push_tag_1st_time_hint() {
	case $1 in
		$PASS)
			return
			;;
		*)
			_tutr_generic_hint $1 git "$_REPO_PATH"
			;;
	esac

	cat <<-MSG

	To push the tag $(ylw final), run $(cmd git push origin final).
	MSG
}

push_tag_1st_time_epilogue() {
	cat <<-MSG
	Great work!  The tag $(ylw final) is now visible on GitLab.
	Switch back to your browser and refresh the page to see for yourself.

	If you already closed that tab, run $(cmd browse_to_repo) to open it again.

	MSG
	_tutr_pressanykey
}



git_help_tag_prologue() {
	cat <<-MSG
	Now that this repository is set up, you are ready to make some tags!

	Tags are manipulated with the $(cmd git tag) subcommand.  $(cmd git tag) can
	do many things, and has a lot of options.

	As always, you can learn all about a subcommand with
	  $(cmd "git help <subcommand>")

	Run $(cmd git help tag) to learn how to print a listing of all tags in the
	repository.  You'll see lots of talk about "tag objects" and "signed
	tags".  Just scroll until you find an option that lets you $(bld List tags).

	MSG
}

git_help_tag_test() {
	_tutr_nonce browse_to_repo && return $PASS
	_tutr_generic_test -c git -a help -a tag
}

git_help_tag_hint() {
	_tutr_generic_hint $1 git "$_REPO_PATH"

	cat <<-MSG

	Run $(cmd git help tag) to learn how to print a listing of all tags.
	MSG
}



list_tags_pre() {
	must_be_in_repo
}

list_tags_prologue() {
	cat <<-MSG
	Think you got it figured out?  Let's see!

	Run a command that lists all tags in this repo.

	Right now, it should print the name of only one tag, namely $(ylw final).
	MSG
}

list_tags_test() {
	if   [[ ${_CMD[0]} == git && ${_CMD[1]} == help ]]; then return $PASS
	elif _tutr_nonce; then return $PASS
	elif [[ ${#_CMD[@]} == 2 && ${_CMD[@]} == "git tag" ]]; then return 0
	elif [[ ${#_CMD[@]} == 3 && ( ${_CMD[@]} == "git tag -l" || ${_CMD[@]} == "git tag --list" ) ]]; then return 0
	else _tutr_generic_test -c git -a tag -d "$_REPO_PATH"
	fi
}

list_tags_hint() {
	_tutr_generic_hint $1 git "$_REPO_PATH"

	cat <<-MSG

	Run a command that lists all tags in this repo.  Right now, it should
	print the name of only one tag, namely $(ylw final).

	If you are stuck, read $(cmd git help tag) again.
	MSG
}

list_tags_epilogue() {
	_tutr_pressanykey

	cat <<-MSG

	Great!

	I know that help page was a lot to wade through.  Reading documentation is
	very important, and finding exactly what you're seeking is a skill that
	improves with practice.

	MSG
	_tutr_pressanykey
}



make_first_tag_rw() {
	git tag -d test0 || true
}

make_first_tag_ff() {
	git tag test0 $_REPO_STARTER_COMMIT
}

make_first_tag_pre() {
	must_be_in_repo
}

make_first_tag_prologue() {
	cat <<-MSG
	At long last, I am finally going to let you make a tag!

	It is not nearly as complicated as $(cmd git help tag) made it seem.
	The syntax for creating a tag is simply
	  $(cmd "git tag <TAGNAME> [commit]")

	* $(ylw "<TAGNAME>") stands in for the name of the tag you will make
	* $(grn "[commit]") is optional.  When you leave this off, the tag is
	  placed on the currently checked out (or $(cyn HEAD)) commit.

	Create a new tag named $(ylw test0) on the latest commit.
	MSG
}

make_first_tag_test() {
	WRONG_COMMIT=99
	TEST1=98

	[[ "$PWD" != "$_REPO_PATH"* ]] && return $WRONG_PWD

	# nonce commands
	if _tutr_nonce; then return $PASS
	elif [[ ${#_CMD[@]} == 2 && ${_CMD[@]} == "git tag" ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git help"* ]]; then return $PASS
	fi

	if git rev-parse --verify --quiet test1 > /dev/null; then
		return $TEST1
	fi

	local TAG
	if TAG=$(git rev-parse --short --verify test0 2> /dev/null); then
		if [[ $TAG == "${_REPO_STARTER_COMMIT}"* ]]; then
			return 0
		else
			return $WRONG_COMMIT
		fi
	else
		# This test shouldn't ever be reached if they correctly apply the tag
		_tutr_generic_test -c git -a tag -a test0
	fi
}

make_first_tag_hint() {
	case $1 in
		$PASS)
			return
			;;

		$TEST1)
			cat <<-MSG
			I asked you to make a tag called $(ylw test0), not $(ylw test1)!

			$(ylw test1) comes later, so be patient!

			I'll just clean up your little mess so you can try again.
			MSG
			git tag -d test1 &> /dev/null
			;;

		$WRONG_COMMIT)
			cat <<-MSG
			Whoops!  You placed that tag on the wrong commit.

			I'll remove it so you can try again.

			Remember, you just need to place it on the currently checked-out
			commit.  It is as easy as ommitting the argument $(grn '[commit]').

			MSG
			git tag -d test0 &> /dev/null
			;;

		*)
			_tutr_generic_hint $1 git "$_REPO_PATH"
			;;
	esac

	cat <<-MSG

	Run $(cmd git tag test0) to tag the current commit.
	MSG
}



git_log_pre() {
	must_be_in_repo
}

git_log_prologue() {
	cat <<-MSG
	Now that you've created your first tag, look at your repository's log
	to see how it looks.
	MSG
}

git_log_test() {
	[[ "$PWD" != "$_REPO_PATH"* ]] && return $WRONG_PWD
	_tutr_nonce && return $PASS
	_tutr_generic_test -c git -a log -x
}

git_log_hint() {
	case $1 in
		$PASS) ;;
		*) _tutr_generic_hint $1 git "$_REPO_PATH" ;;
	esac

	cat <<-MSG

	Run $(cmd git log) to see your new tag
	MSG
}

git_log_epilogue() {
	cat <<-MSG
	As you can see, $(ylw test0) has been added to the most recent
	commit, right alongside $(ylw final).

	There is no limit to the number of tags that can be attached to a
	commit.  This comes in handy when one commit represents multiple
	milestones in a project's lifecycle.

	MSG

	_tutr_pressanykey
}


make_second_tag_rw() {
	git tag -d test1 || true
}

make_second_tag_ff() {
	git tag test1 $_REPO_2ND_COMMIT
}

make_second_tag_pre() {
	must_be_in_repo
}

make_second_tag_prologue() {
	cat <<-MSG
	Next, you'll place a tag on a commit that's not currently checked-out.

	Tag the $(bld second-most) recent commit $(ylw test1).  To do this, you will use
	$(cmd git tag)'s optional $(grn '[commit]') argument.

	There are a few ways to specify a $(grn '[commit]') that is not checked-out.
	I'll teach you the most straight-forward one: the $(ylw_ SHA-1 fingerprint).

	MSG

	_tutr_pressanykey

	cat <<-MSG

	You've already seen these in the $(cmd git log):

	  $(ylw_ commit $_REPO_STARTER_COMMIT) ($(cyn "HEAD ->") $(grn master), $(ylw tag: final), $(_remote origin/master)$(ylw_ ,) $(_remote origin/HEAD)$(ylw_ ")")
	  Author: Jaxton Winder <jjwinder9@gmail.com>
	  Date:   2022-07-05 19:35:25 -0600

	Git generates a unique "name" for every commit that is created.  They
	are called different things by different people: hashes, checksums, and
	cryptographic IDs.  These IDs are 40 characters long and are formed from
	the ten digits $(mgn_ 0-9) and the six letters $(mgn_ a, b, c, d, e, f).

	Like your own fingerprints, these IDs are unique.  Their uniqueness
	makes them useful, but not very human-friendly.  Fortunately, Git's
	fingerprints are $(bld so) unique that you can get away with abbreviating
	them down to their first 7 or 8 characters.

	But we can do better.  It is much easier to remember $(ylw final) than
	$(ylw_ $_REPO_STARTER_COMMIT_L) or even $(ylw_ $_REPO_STARTER_COMMIT).
	This is one reason why Git has tags.  However, in order to tag an older
	commit with a memorable name, you still need to learn its fingerprint.

	MSG

	_tutr_pressanykey

	cat <<-MSG

	Add a tag named $(ylw test1) to the $(bld second-most) recent commit.

	Use $(cmd git log) to find that commit's SHA-1 fingerprint, then run
	  $(cmd "git tag <TAGNAME> <SHA-1>") to tag it.
	MSG
}

make_second_tag_test() {
	ON_WRONG_COMMIT=99
	BACKWARDS_CMD=98

	[[ "$PWD" != "$_REPO_PATH"* ]] && return $WRONG_PWD

	# Check nonce commands
	if [[ ${_CMD[*]} == "git log"* ]]; then return $PASS
	elif _tutr_nonce; then return $PASS
	fi

	if [[ ${_CMD[0]} == git && \
		  ${_CMD[1]} == tag && \
		  ${_REPO_2ND_COMMIT_L} == "${_CMD[2]}"* && \
		  ${_CMD[3]} == test1 ]]; then
		return $BACKWARDS_CMD
	fi

	local TAG_ON_COMMIT=$(git rev-parse --short test1 2> /dev/null)
	if ! [[ -z $TAG_ON_COMMIT ]]; then
		if [[ $TAG_ON_COMMIT == "${_REPO_2ND_COMMIT}"* ]]; then
			return 0
		else
			return $ON_WRONG_COMMIT
		fi
	else
		# This test shouldn't ever be reached if they correctly apply the tag
		_tutr_generic_test -c git -a tag -a test1 -a $_REPO_2ND_COMMIT
	fi
}

make_second_tag_hint() {
	case $1 in
		$PASS)
			return
			;;

		$BACKWARDS_CMD)
			cat <<-MSG
			You wrote that backwards.

			The command goes like this:
			  $(cmd "git tag <TAGNAME> <SHA-1>")

			And your command was:
			  $(cmd "git tag <SHA-1> <TAGNAME>")

			Switch your pitch up, and try again.
			MSG
			return
			;;

		$ON_WRONG_COMMIT)
			cat <<-MSG
			Whoops!  You tagged the wrong commit.

			I'll remove it so you can try again.

			You need to tag the $(bld second) most-recent commit using $(cmd git tag)'s
			$(grn '[commit]') argument.

			MSG
			git tag -d test1 &> /dev/null || true
			;;

		*)
			_tutr_generic_hint $1 git "$_REPO_PATH"
			;;
	esac

	cat <<-MSG

	To find the SHA-1 fingerprint of the $(bld second) most-recent commit, consult
	the $(cmd git log).  You only need to copy the first 7 characters.
	MSG
}

make_second_tag_epilogue() {
	echo "Good job!"
}


warn_about_https_prompts() {
	# Because student used https url instead of ssh url, some steps that run
	#	'git ls-remote' in their test might require extra login prompts
	cat <<-MSG
	For this step, the shell tutor is going to need to speak to your Git
	$(_remote) to verify things were done correctly. It appears you used an
	HTTPS URL instead of an SSH URL to connect your $(_remote). This is going
	to result in you getting prompted to input your username and password
	for GitLab at various points during this step. This is normal
	behavior, despite being a bit annoying.

	I would highly recommend using SSH URL's for your git $(_remote remotes) in the
	future.  SSH handles authentication automatically so you won't need to
	repeatedly type your username and password.
	MSG
}

push_all_tags_rw() {
	git push origin -d test0 test1
}

push_all_tags_ff() {
	git push origin test0 test1
}

push_all_tags_pre() {
	must_be_in_repo
	if [[ "$(git remote -v | command grep origin)" == *"https://"* ]]; then
		_tutr_warn warn_about_https_prompts
	fi
}

push_all_tags_prologue() {
	cat <<-MSG
	Now you will push both tags up to GitLab.

	You can push each tag individually, like this:
	  $(cmd git push origin test0)
	  $(cmd git push origin test1)

	Or, you can do it in one line by spelling out all of the names:
	  $(cmd git push origin test0 test1)

	Maybe you have a whole bunch of tags to push, and you can't remember all
	of their names.  You can be super lazy and give $(cmd git push) a $(cyn really fancy)
	argument that pushes every tag at once:
	  $(cmd git push origin $(cyn --tags))

	When pushing to the default $(_remote) (defined with $(cmd git push -u)), you can
	omit $(_origin) from the last command:
	  $(cmd git push $(cyn --tags))

	Push those tags using whichever technique trips your trigger.
	MSG
}

push_all_tags_test() {
	ON_WRONG_COMMIT=99
	AT_LEAST_ONE_TAG_NOT_PUSHED=98

	[[ "$PWD" != "$_REPO_PATH"* ]] && return $WRONG_PWD

	if _tutr_nonce; then return $PASS
	elif [[ "${_CMD[@]}" == "git log"* ]]; then return $PASS
	elif [[ ${_CMD[*]} == *"--tags" ]]; then
		if (( ${#_CMD[@]} == 3)); then
			_tutr_generic_test -c git -a push -a "--tags"
		else
			_tutr_generic_test -c git -a push -a origin -a "--tags"
		fi
	elif [[ ${_CMD[*]} == "git remote"* ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git help"* ]]; then return $PASS
	else
		git ls-remote origin &> .ls-remote
		TEST0_REF=$(command grep test0 .ls-remote | cut -f1)
		TEST1_REF=$(command grep test1 .ls-remote | cut -f1)

		if [[ -n $TEST0_REF && -n $TEST1_REF ]]; then
			if [[ $TEST0_REF == $_REPO_STARTER_COMMIT_L &&
				  $TEST1_REF == $_REPO_2ND_COMMIT_L ]]; then
				# Both tags are on gitlab and on the correct commits! Woo!
				return 0
			else
				return $ON_WRONG_COMMIT
			fi
		else
			return $AT_LEAST_ONE_TAG_NOT_PUSHED
		fi
	fi
}

push_all_tags_hint() {
	case $1 in
		$PASS)
			return
			;;
		$AT_LEAST_ONE_TAG_NOT_PUSHED)
			cat <<-MSG
			One (or both) tags are not pushed to GitLab.  Be sure to push both
			tags to GitLab!
			MSG
			;;

		$ON_WRONG_COMMIT)
			cat <<-MSG
			${_y}         ,^,
			${_y}       ,;   ;,         ${_Z}Well... this is awkward.  One
			${_y}     ,; ,---, ;,       ${_Z}(or both) of your tags are on
			${_y}   ,; ,'.---,\\  ;,     ${_Z}the wrong commits.
			${_y} ,;   | |   | |   ;,   ${_Z}
			${_y}<    ,| |,  | |     >  ${_Z}You need to identify which tag
			${_y} ';   \\ /   | |   ;'   ${_Z}is on the wrong commit, then
			${_y}   ';  V    |_| ;'     ${_Z}$(bld "git push -d <TAGNAME>")
			${_y}     ';       ;'       ${_Z}to delete it.
			${_y}       ';   ;'
			${_y}         'V'           ${_Z}Afterward, re-tag those commits:

			* $(ylw test0) should be on $(ylw_ $_REPO_STARTER_COMMIT)
			* $(ylw test1) should be on $(ylw_ $_REPO_2ND_COMMIT)

			MSG
			;;
		*)
			_tutr_generic_hint $1 git "$_REPO_PATH"
			;;
	esac
}

push_all_tags_epilogue() {
	cat <<-MSG
	Great work!  Your new tags are now on GitLab.

	Refresh your browser window (or run $(bld browse_to_repo)) to see them.
	MSG
}



make_new_commit_rw() {
	git reset --hard $_REPO_STARTER_COMMIT
}

make_new_commit_ff() {
	date >> "$_REPO_PATH/TODO.md"
	git commit -am "an automatic change"
}

make_new_commit_prologue() {
	cat <<-MSG
	Now I want you to tag a $(bld new) commit of your very own.

	Make a change to $(_md TODO.md), then $(cmd git add) and $(cmd git commit) it.
	MSG
}

make_new_commit_test() {
	[[ "$PWD" != "$_REPO_PATH"* ]] && return $WRONG_PWD
	EDITED=99
	ADDED=98

	local _EDITORS=(nano vim vi nvim open emacs code pycharm pycharm.sh charm)
	if _tutr_nonce; then return $PASS
	elif _tutr_nonce ${_EDITORS[@]}; then return $EDITED
	elif [[ ${_CMD[*]} == "git add"* ]]; then return $ADDED
	elif [[ ${_CMD[*]} == "git status"* ]]; then return $PASS
	else
		MASTER_ON_COMMIT=$(git rev-parse --short master)
		if [[ $MASTER_ON_COMMIT != "$_REPO_STARTER_COMMIT"* ]]; then
			return 0
		else
			return $WRONG_CMD
		fi
	fi
}

make_new_commit_hint() {
	case $1 in
		$PASS)
			return
			;;
		$WRONG_PWD)
			cat <<-MSG
			You left the repository.

			MSG
			_tutr_minimal_chdir_hint "$_REPO_PATH"
			;;

		$EDITED)
			cat <<-MSG
			Now run $(cmd git add TODO.md) to stage your change.
			MSG
			;;

		$ADDED)
			cat <<-MSG
			Permanently record this new commit with $(cmd "git commit -m 'COMMIT MESSAGE'")
			MSG
			;;

		*)
			cat <<-MSG
			There is a file here named $(path TODO.md) Open it in your
			favorite text editor and make a change.

			Then run $(cmd git add TODO.md) to stage your change.

			Finally, use $(cmd git commit -m "COMMIT_MSG") to save the new commit.

			$(cmd git status) will display the status of your repository at any
			time.  This will show you any unstaged and uncommitted changes.
			MSG
			;;
	esac
}


move_final_tag_failure_rw() {
	git tag -f final $_REPO_STARTER_COMMIT
}

move_final_tag_failure_ff() {
	git tag -f final
}

move_final_tag_failure_pre() {
	[[ -n $STUDENT_IS_VERY_CLEVER ]] && unset STUDENT_IS_VERY_CLEVER
}

move_final_tag_failure_prologue() {
	cat <<-MSG
	Now that we have a new commit made, we should probably adjust that
	$(ylw final) tag, right?

	Run $(bld git tag final) to put a new $(ylw final) tag on your newest commit.
	MSG
}

move_final_tag_failure_test() {
	[[ "$PWD" != "$_REPO_PATH"* ]] && return $WRONG_PWD

	if _tutr_nonce; then return $PASS
	elif [[ ${_CMD[*]} == "git log"* ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git status" ]]; then return $PASS
	elif [[ $(git rev-parse --short master 2> /dev/null) == $(git rev-parse --short final 2> /dev/null) ]]; then
		# That crafty student found out about the '-f' option!
		STUDENT_IS_VERY_CLEVER=true
		return 0
	fi
	_tutr_generic_test -c git -a tag -a final -f -x
}

move_final_tag_failure_hint() {
	case $1 in
		$PASS)
			return
			;;
		*)
			_tutr_generic_hint $1 git $_REPO_PATH
			;;
	esac
}

move_final_tag_failure_epilogue() {
	if [[ -n $STUDENT_IS_VERY_CLEVER ]]; then
		cat <<-MSG
		... I'm impressed.${_M}    ___            ___
		                  ${_M}   / _ \\__      __/ _ \\
		                  ${_M}  | | | \\ \\ /\\ / / | | |
		                  ${_M}  | |_| |\\ V  V /| |_| |
		                  ${_M}   \\___/  \\_/\\_/  \\___/${_Z}

		I thought I could trick you into running a command that would fail,
		and make a point of learning from your mistakes.

		Clearly, I underestimated you Git-foo.

		$(bld Welcome to Warp Zone!)  This'll skip you ahead a few steps...

		MSG
	else
		_tutr_pressanykey
		cat <<-MSG

		You can learn a lot from a failed command!

		Because a tag called $(ylw final) already exists, you can't make another
		with the same name.  However, you $(bld still) need to move $(ylw final) to the
		newest commit.

		You'll just need to find another way.

		MSG
	fi
	_tutr_pressanykey
}



delete_final_tag_rw() {
	git tag -f final $_REPO_STARTER_COMMIT
}

delete_final_tag_ff() {
	git tag -d final
}

delete_final_tag_pre() {
	must_be_in_repo
}

delete_final_tag_prologue() {
	cat <<-MSG
	Moving a tag is done in two steps:

	First, you $(bld delete) the tag
	Then, you $(bld re-create) it on a new commit.

	Review $(cmd git help tag) to find out how to $(bld delete) $(ylw final).
	MSG
}

delete_final_tag_test() {
	TAG_STILL_THERE=99
	HELPED=98

	[[ "$PWD" != "$_REPO_PATH"* ]] && return $WRONG_PWD

	if _tutr_nonce; then return $PASS
	elif [[ ${_CMD[@]} == "git help tag" ]]; then return $HELPED
	elif [[ $(git rev-parse --short master 2> /dev/null) == $(git rev-parse --short final 2> /dev/null) ]]; then
		# clever student can skip this step! They don't need to delete the 'final' tag, it's already on the right commit
		return 0
	else
		if [[ -z $(git tag -l final) ]]; then
			return 0
		else
			return $TAG_STILL_THERE
		fi
	fi
}

delete_final_tag_hint() {
	case $1 in
		$PASS) ;;
		$HELPED)
			cat <<-MSG
			Did you find what you were looking for in the help page?

			Give it a shot!
			MSG
			;;

		$TAG_STILL_THERE)
			cat <<-MSG
			Hmmm... looks like you haven't deleted $(ylw final) yet.
			Try $(cmd git tag -d final) to delete it from your $(_local) repo.
			MSG
			;;

		*)
			_tutr_generic_hint $1 git "$_REPO_PATH"
			;;
	esac
}

delete_final_tag_epilogue() {
	cat <<-MSG
	Nailed it!

	MSG
	_tutr_pressanykey
}



move_final_tag_correctly_rw() {
	git tag -d final
}

move_final_tag_correctly_ff() {
	git tag final
}

move_final_tag_correctly_pre() {
	must_be_in_repo
}


move_final_tag_correctly_prologue() {
	cat <<-MSG
	Now, tag the most recent commit as $(ylw final).
	MSG
}

move_final_tag_correctly_test() {
	FINAL_DOESNT_EXIST=99
	FINAL_ON_WRONG_COMMIT=98
	DELETED=97

	[[ "$PWD" != "$_REPO_PATH"* ]] && return $WRONG_PWD

	# Whole bunch of nonce commands to ignore
	if _tutr_nonce; then return $PASS
	elif [[ ${_CMD[*]} == "git status" ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git log"* ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git tag -l" ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git tag -d"* ]]; then return $DELETED
	elif [[ ${_CMD[*]} == "git remote"* ]]; then return $PASS
	fi

	local MASTER=$(git rev-parse --short master 2> /dev/null)
	local FINAL=$(git rev-parse --short final 2> /dev/null)
	if [[ -z $FINAL ]]; then return $FINAL_DOESNT_EXIST
	elif [[ $MASTER == $FINAL ]]; then return 0
	elif [[ $MASTER != $FINAL ]]; then return $FINAL_ON_WRONG_COMMIT
	else
		_tutr_generic_test -c git -a tag -a final -x
	fi
}

move_final_tag_correctly_hint() {
	case $1 in
		$PASS)
			return
			;;

		$FINAL_DOESNT_EXIST)
			cat <<-MSG
			You haven't placed $(ylw final) on any commit.  Tag it on the
			newest commit by running $(cmd git tag final).
			MSG
			;;

		$FINAL_ON_WRONG_COMMIT)
			cat <<-MSG
			You tagged $(ylw final) on the wrong commit.

			Delete it with $(cmd git tag -d final), then re-tag the latest commit
			by running $(cmd git tag final).
			MSG
			;;

		$DELETED)
			cat <<-MSG
			Now, tag the newest commit $(ylw final).
			MSG
			;;
		*)
			_tutr_generic_hint $1 git "$_REPO_PATH"
			;;
	esac
}




push_final_tag_fail_pre() {
	must_be_in_repo
	[[ -n $STUDENT_IS_TOO_CLEVER_FOR_THEIR_OWN_GOOD ]] && unset STUDENT_IS_TOO_CLEVER_FOR_THEIR_OWN_GOOD
}

push_final_tag_fail_prologue() {
	cat <<-MSG
	Now you can push $(ylw final) back up to GitLab.
	MSG
}

push_final_tag_fail_test() {
	[[ "$PWD" != "$_REPO_PATH"* ]] && return $WRONG_PWD

	if _tutr_nonce; then return $PASS
	elif [[ ${_CMD[*]} == "git status" ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git log"* ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git help"* ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git tag" ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git tag --list" ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git tag -l" ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git tag -d"* ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git remote"* ]]; then return $PASS
	fi

	if [[ ${_CMD[*]} == *"--tags" ]]; then
		if (( ${#_CMD[@]} == 3 )); then
			_tutr_generic_test -c git -a push -a "--tags" -f
		else
			_tutr_generic_test -c git -a push -a origin -a "--tags" -f
		fi
	elif [[ ${_CMD[*]} == "git push"* && ${_CMD[*]} == *"-f"* ]]; then
		# THAT SNEAKY STUDENT DID A FORCE PUSH
		#	The Jedi academy might be interested in their special set of skills... /s
		git ls-remote origin &> .ls-remote
		MASTER_IS_AT=$(git rev-parse --short master 2> /dev/null)
		FINAL_REMOTE_TAG_REF=$(command grep final .ls-remote | cut -f1)
		if [[ $FINAL_REMOTE_TAG_REF == "$MASTER_IS_AT"* ]]; then
			STUDENT_IS_TOO_CLEVER_FOR_THEIR_OWN_GOOD=true
			return 0
		else
			return $WRONG_CMD_ARGS
		fi
	else
		_tutr_generic_test -c git -a push -a origin -a final -f
	fi
}

push_final_tag_fail_hint() {
	case $1 in
		$PASS)
			;;
		*)
			_tutr_generic_hint $1 git $_REPO_PATH
			;;
	esac
}

push_final_tag_fail_epilogue() {
	if [[ -n $STUDENT_IS_TOO_CLEVER_FOR_THEIR_OWN_GOOD ]]; then
		cat <<-MSG
		You did WHAT?  ${_R}     ___         ___
		               ${_R}    / _ \\ _ __  / _ \\
		               ${_R}   | | | | '_ \\| | | |
		               ${_R}   | |_| | | | | |_| |
		               ${_R}    \\___/|_| |_|\\___/${_Z}

		I must admit, I am impressed that you know about force pushes.
		Maybe the Jedi academy has an opening for you?

		Force pushes are $(bld very) dangerous in practice, especially in
		repositories that are shared with others.  I don't recommend force
		pushes.  If anyone asks, you didn't learn about them from me.

		To be quite honest, I expected your $(cmd git push) to fail as a set-up
		to teach you how to delete that tag from the $(_remote) repository with
		$(cmd git push -d final)

		I guess that teaching opportunity is moot now?  I'll just fast-track
		you to the end of the lesson.
		MSG
	else
		cat <<-MSG
		I seem to have set you up for failure... as a learning opportunity.

		You can't push $(ylw final) to the $(_remote) repository because it
		is already there!  In the same way that you were unable to have two
		$(ylw final) tags in your $(_local) repository, you cannot have the same
		tags on two commits on the $(_remote) repository.

		Just like before, it is fixed in two steps: a $(bld deletion) followed
		by a $(bld re-creation).
		MSG
	fi
	_tutr_pressanykey
}



push_delete_tag_pre() {
	must_be_in_repo
}

push_delete_tag_prologue() {
	cat <<-MSG
	Deleting a tag on a $(_remote) repository is accomplished with $(cmd git push),
	and not with a variation of $(cmd git tag).

	Surprised?  I was when I first learned this.

	$(cmd "git push -d <remote> <tag>") reaches out to the server at $(red "<remote>")
	and asks it to delete $(ylw "<tag>").

	You're ready to delete $(ylw final) from $(_origin) now.
	MSG
}

push_delete_tag_test() {
	WRONG_DELETE=99

	if [[ -n $STUDENT_IS_TOO_CLEVER_FOR_THEIR_OWN_GOOD ]]; then
		# Student used a force push earlier, so they can skip this step
		return 0
	fi

	[[ "$PWD" != "$_REPO_PATH"* ]] && return $WRONG_PWD

	if _tutr_nonce; then return $PASS
	elif [[ ${_CMD[*]} == "git status" ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git log"* ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git help"* ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git tag -l" ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git tag --list" ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git tag" ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git remote"* ]]; then return $PASS
	fi

	if [[ ${_CMD[*]} == "git tag -d"* ]]; then return $WRONG_DELETE
	elif [[ ${_CMD[*]} == "git push"* ]]; then
		# There's a few ways to delete this tag with 'git push', so I don't
		#	want to be too rigid in my test
		git ls-remote origin &> .ls-remote
		FINAL_REMOTE_TAG_REF=$(command grep final .ls-remote | cut -f1)
		if [[ -z $FINAL_REMOTE_TAG_REF ]]; then
			return 0
		fi
	fi
	_tutr_generic_test -c git -a push -a "-d" -a origin -a final -d "$_REPO_PATH"
}

push_delete_tag_hint() {
	case $1 in
		$PASS)
			;;
		$WRONG_DELETE)
			cat <<-MSG
			You used the wrong $(bld delete) command!  If you just accidentally
			deleted $(ylw final) from your $(_local) repository, replace it before
			continuing with $(cmd git push -d origin final).

			You can tell if you deleted $(ylw final) by checking $(cmd git log) or
			$(cmd git tag).

			MSG
			_tutr_pressanykey
			;;
		*)
			_tutr_generic_hint $1 git "$_REPO_PATH"
			;;
	esac
}


push_delete_tag_epilogue() {
	cat <<-MSG
	Now that $(ylw final) is deleted from the $(_remote), you've made room
	to put it in its right place.

	MSG
	_tutr_pressanykey
}



push_final_tag_success_prologue() {
	cat <<-MSG
	At last, you can push $(ylw final) up to GitLab.
	MSG
}

push_final_tag_success_test() {
	if [[ -n $STUDENT_IS_TOO_CLEVER_FOR_THEIR_OWN_GOOD ]]; then
		# Student used a force push earlier, so they can skip this step
		return 0
	fi
	ON_WRONG_COMMIT=99
	TAG_NOT_PUSHED=98

	[[ "$PWD" != "$_REPO_PATH"* ]] && return $WRONG_PWD

	if _tutr_nonce; then return $PASS
	elif [[ ${_CMD[*]} == *"--tags" ]]; then
		if (( ${#_CMD[@]} == 3)); then
			_tutr_generic_test -c git -a push -a "--tags"
		else
			_tutr_generic_test -c git -a push -a origin -a "--tags"
		fi
	elif [[ ${_CMD[*]} == "git remote"* ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git log"* ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git help"* ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git push -d"* ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git tag"* ]]; then return $PASS
	else
		git ls-remote origin &> .ls-remote
		MASTER_IS_AT=$(git rev-parse --short master 2> /dev/null)
		FINAL_TAG_REF=$(command grep final .ls-remote | cut -f1)

		if [[ $FINAL_TAG_REF == "$MASTER_IS_AT"* ]]; then
			return 0
		elif [[ -z $FINAL_REMOTE_TAG_REF ]]; then
			return $TAG_NOT_PUSHED
		else
			return $ON_WRONG_COMMIT
		fi
	fi
}

push_final_tag_success_hint() {
	case $1 in
		$PASS)
			;;
		$ON_WRONG_COMMIT)
			cat <<-MSG
			${_y}         ,^,
			${_y}       ,;   ;,         ${_Z}Well... this is awkward.  The wrong commit has
			${_y}     ,; ,---, ;,       ${_Z}been tagged $(ylw final).
			${_y}   ,; ,'.---,\\  ;,     ${_Z}
			${_y} ,;   | |   | |   ;,   ${_Z}I'm not sure how this happened, but $(ylw final)
			${_y}<    ,| |,  | |     >  ${_Z}needs to be replaced on the $(_remote) repo.  First,
			${_y} ';   \\ /   | |   ;'   ${_Z}delete it on GitLab with $(cmd git push -d origin final)
			${_y}   ';  V    |_| ;'     ${_Z}
			${_y}     ';       ;'       ${_Z}Then delete it $(_local locally): $(cmd git tag -d final)
			${_y}       ';   ;'         ${_Z}
			${_y}         'V'           ${_Z}Finally, re-tag the latest commit: $(cmd git tag final)
			MSG
			;;

		$TAG_NOT_PUSHED)
			cat <<-MSG
			The $(ylw final) tag has yet to be pushed to the $(_remote).
			Push it with $(cmd git push origin final).
			MSG
			;;

		*)
			_tutr_generic_hint $1 git "$_REPO_PATH"
			;;
	esac
}

push_final_tag_success_epilogue() {
	cat <<-MSG
	Great work!  Your $(ylw final) tag is updated on GitLab.

	Run $(cmd browse_to_repo) to see it in your browser.

	MSG
	_tutr_pressanykey
}



push_final_commit_prologue() {
	cat <<-MSG
	As you check out your $(_remote) repository in the browser, you should notice
	that something is missing... that new commit you just made!

	By default, GitLab shows the latest commit $(bld on the default branch),
	which is called $(grn master).  You only told Git to push the $(ylw final) tag, so the
	$(_origin origin remote) hasn't updated its own $(grn master) branch to match yours.

	This may seem a bit strange (because it is), but it is something that
	you need to be aware of.  The rule of thumb is that Git always expects
	you to $(bld be explicit about what you want to happen).  If you don't tell
	Git $(bld exactly) what to do, it doesn't happen.

	Because you didn't $(bld explicitly) push $(grn master), it is not updated.

	You can fix this with either $(cmd git push) or $(cmd git push origin master).
	This will send your $(grn master) branch to GitLab, including your last commit.
	MSG
}

push_final_commit_test() {
	[[ "$PWD" != "$_REPO_PATH"* ]] && return $WRONG_PWD
	git ls-remote origin &> .ls-remote
	local LOCAL_MASTER=$(git rev-parse master 2> /dev/null)
	local REMOTE_MASTER=$(command grep master .ls-remote | cut -f1)

	if   [[ $LOCAL_MASTER == $REMOTE_MASTER ]]; then return 0
	elif _tutr_nonce; then return $PASS
	elif [[ ${_CMD[*]} == "git remote"* ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git log"* ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git help"* ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git push -d"* ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git tag"* ]]; then return $PASS

	# Should I do the ls-remote stuff here, or will the generic test suffice?
	else _tutr_generic_test -c git -a push -x -d "$_REPO_PATH"
	fi
}

push_final_commit_hint() {
	case $1 in
		$PASS) ;;
		*) _tutr_generic_hint $1 git "$_REPO_PATH" ;;
	esac
}


epilogue() {
	cat <<-EPILOGUE
	${_C}  _____                        __       __     __  _
	${_C} / ___/__  ___  ___ ________ _/ /___ __/ /__ _/ /_(_)__  ___  ___
	${_C}/ /__/ _ \\/ _ \\/ _ \`/ __/ _ \`/ __/ // / / _ \`/ __/ / _ \\/ _ \\(_-<
	${_C}\\___/\\___/_//_/\\_, /_/  \\_,_/\\__/\\_,_/_/\\_,_/\\__/_/\\___/_//_/___/
	${_C}              /___/

	      ${_Y}   ________${_Z}
	      ${_Y}  |        |${_Z}
	      ${_Y} /|   #1   |\\${_Z}  Phenomenal work!
	      ${_Y}( |  GIT   | )${_Z}
	      ${_Y} \\| CHAMP! |/${_Z}  You now know the basics of Git tagging.
	      ${_Y}   \\      /${_Z}    Git is becoming second nature to you!
	      ${_Y}    \`+--+'${_Z}
	      ${_Y}     |  |${_Z}
	      ${_Y}    _|__|_${_Z}


	FYI, the $(path $_REPO_NAME) repository that you cloned in this lesson will now
	be erased from your computer.  It is still on your account on GitLab.

	Run $(cmd ${SHELL##*/} 1-project-tags.sh) to enter the next lesson

	EPILOGUE

	_tutr_pressanykey
}


cleanup() {
	if [[ -d "$_REPO_PATH" ]]; then
		echo "Cleaning up $_REPO_PATH..."
		rm -rf "$_REPO_PATH"
	fi

	if [[ -d /tmp/tags ]]; then
		echo "Cleaning up /tmp/tags..."
		rm -rf /tmp/tags
	fi

	# Remember that this lesson has been completed
	(( $# >= 1 && $1 == $_COMPLETE)) && _tutr_record_completion ${_TUTR#./}
	echo "You studied Git tag syntax for $(_tutr_pretty_time)"
}


source main.sh \
	cd_dotdot \
	clone_repository \
	cd_into_repo \
	ls_inspect_repo \
	inspect_repo \
	remote_rename \
	remote_add \
	push_repo \
	push_tag_1st_time \
	git_help_tag \
	list_tags \
	make_first_tag \
	git_log \
	make_second_tag \
	push_all_tags \
	make_new_commit \
	move_final_tag_failure \
	delete_final_tag \
	move_final_tag_correctly \
	push_final_tag_fail \
	push_delete_tag \
	push_final_tag_success \
	push_final_commit


# vim: set filetype=sh noexpandtab tabstop=4 shiftwidth=4 textwidth=0 colorcolumn=76:
