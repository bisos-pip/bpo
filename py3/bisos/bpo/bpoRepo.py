# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: A =CS-Lib= for creating and managing symetric gpg  encryption/decryption.
#+end_org """

####+BEGIN: b:py3:cs:file/dblockControls :classification "cs-u"
""" #+begin_org
* [[elisp:(org-cycle)][| /Control Parameters Of This File/ |]] :: dblk ctrls classifications=cs-u
#+BEGIN_SRC emacs-lisp
(setq-local b:dblockControls t) ; (setq-local b:dblockControls nil)
(put 'b:dblockControls 'py3:cs:Classification "cs-u") ; one of cs-mu, cs-u, cs-lib, bpf-lib, pyLibPure
#+END_SRC
#+RESULTS:
: cs-u
#+end_org """
####+END:

####+BEGIN: b:prog:file/proclamations :outLevel 1
""" #+begin_org
* *[[elisp:(org-cycle)][| Proclamations |]]* :: Libre-Halaal Software --- Part Of BISOS ---  Poly-COMEEGA Format.
** This is Libre-Halaal Software. © Neda Communications, Inc. Subject to AGPL.
** It is part of BISOS (ByStar Internet Services OS)
** Best read and edited  with Blee in Poly-COMEEGA (Polymode Colaborative Org-Mode Enhance Emacs Generalized Authorship)
#+end_org """
####+END:

####+BEGIN: b:prog:file/particulars :authors ("./inserts/authors-mb.org")
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars |]]* :: Authors, version
** This File: /bisos/git/auth/bxRepos/bisos-pip/bpo/py3/bisos/bpo/bpo.py
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:python:file/particulars-csInfo :status "inUse"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
import typing
csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['bpo'], }
csInfo['version'] = '202210010431'
csInfo['status']  = 'inUse'
csInfo['panel'] = 'bpo-Panel.org'
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* /[[elisp:(org-cycle)][| Description |]]/ :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/PyFwrk/bisos.crypt/_nodeBase_/fullUsagePanel-en.org][PyFwrk bisos.crypt Panel]]
Module description comes here.
** Relevant Panels:
** Status: In use with blee3
** /[[elisp:(org-cycle)][| Planned Improvements |]]/ :
*** TODO complete fileName in particulars.
#+end_org """

####+BEGIN: b:prog:file/orgTopControls :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Controls |]] :: [[elisp:(delete-other-windows)][(1)]] | [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
#+end_org """
####+END:

####+BEGIN: b:python:file/workbench :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Workbench |]] :: [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pydoc ./%s" (bx:buf-fname))))][pydoc]] || [[elisp:(python-check (format "/bisos/pipx/bin/pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "/bisos/pipx/bin/pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "/bisos/pipx/bin/pycodestyle %s" (bx:buf-fname))))][pycodestyle]] | [[elisp:(python-check (format "/bisos/pipx/bin/flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "/bisos/pipx/bin/pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:orgItem/basic :type "=PyImports= " :title "*Py Library IMPORTS*" :comment "-- with classification based framework/imports"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =PyImports=  [[elisp:(outline-show-subtree+toggle)][||]] *Py Library IMPORTS* -- with classification based framework/imports  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:framework/imports :basedOn "classification"
""" #+begin_org
** Imports Based On Classification=cs-u
#+end_org """
from bisos import b
from bisos.b import cs
from bisos.b import b_io

import collections
####+END:

from bisos.bpo import bpo

import os
import enum

from bisos.basics import pattern

####+BEGIN: bx:dblock:python:section :title "Enumerations"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Enumerations*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:

####+BEGIN: b:py3:class/decl :className "BpoRepo" :superClass "object" :comment "A BPO Repository -- to be subclassed" :classType "basic"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-basic  [[elisp:(outline-show-subtree+toggle)][||]] /BpoRepo/  superClass=object =A BPO Repository -- to be subclassed=  [[elisp:(org-cycle)][| ]]
#+end_org """
class BpoRepo(object):
####+END:
    """
** Abstraction of the base ByStar Portable Object
"""

    def __init__(
            self,
            bpoId="__orRepoPath",
            bpoRepoName="__orRepoPath",
            bpoRepoPath="__orBpoIdAnBpoRepoName"
    ):
        self.bpoId = None
        self.bpoRepoName = None
        self.bpoRepoPath = None
        if bpoId == "__orRepoPath" or  bpoRepoName == "__orRepoPath":
            if bpoRepoPath == "__orBpoIdAnBpoRepoName":
                b_io.eh.critical_usageError("Bad Usage")
                # eh.exit()
            self.bpoRepoPath = bpoRepoPath

        if bpoRepoPath == "__orBpoIdAnBpoRepoName":
            if bpoId == "__orRepoPath" or  bpoRepoName == "__orRepoPath":
                b_io.eh.critical_usageError("Bad Usage")
                # eh.exit()
            self.bpoId = bpoId
            self.bpoRepoName = bpoRepoName

        self.prepare()

    def prepare(self,) -> None:
        if self.bpoId is None:
            if self.bpoRepoName is not None:
                b_io.eh.critical_oops("")
            # NOTYET, based on path determine them
            # bpoReposManage.sh -h -v -n showRun -i bpoIdObtainForPath .

        if self.bpoRepoPath is None:
            self.bpoRepoPath = "NOTYET, self.bpoId+self.bpoRepoName"

    def repoCreateAndPush_withIcm(self,):
        pass
        # bpoReposManage.sh -h -v -n showRun -i repoCreateAndPushBasedOnPath

    def repoCreateAndPush(self,):
        pass
        # bpoReposManage.sh -h -v -n showRun -i repoCreateAndPushBasedOnPath

    def repoDelete(self,):
        pass
        # bpoReposManage.sh -h -v -n showRun -i repoCreateAndPushBasedOnPath

    def repoStatus(self,):
        pass
        # bpoReposManage.sh -h -v -n showRun -i repoCreateAndPushBasedOnPath

    def repoClone(self,):
        pass
        # bpoReposManage.sh -h -v -n showRun -i repoCreateAndPushBasedOnPath

    def repoPush(self,):
        pass
        # bpoReposManage.sh -h -v -n showRun -i repoCreateAndPushBasedOnPath

    def repoPull(self,):
        pass
        # bpoReposManage.sh -h -v -n showRun -i repoCreateAndPushBasedOnPath





####+BEGIN: b:py3:class/decl :className "BpoRepo_Rbxe" :superClass "BpoRepo" :comment "A BPO Repository -- to be subclassed" :classType "basic"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-basic  [[elisp:(outline-show-subtree+toggle)][||]] /BpoRepo_Rbxe/  superClass=BpoRepo =A BPO Repository -- to be subclassed=  [[elisp:(org-cycle)][| ]]
#+end_org """
class BpoRepo_Rbxe(BpoRepo):
####+END:
    """
** Abstraction of the base ByStar Portable Object
"""
    def __init__(
            self,
            bpoId,
    ):
        super().__init__(bpoId)
        if not EffectiveBpos.givenBpoIdGetBpo(bpoId):
            b_io.eh.critical_usageError(f"Missing BPO for {bpoId}")
            return

    def info(self,):
        print(f"rbxeInfo bpoId={self.bpo.bpoId}") # type: ignore


####+BEGIN: b:py3:class/decl :className "BpoRepo_BxeTree" :superClass "BpoRepo" :comment "A BPO Repository -- to be subclassed" :classType "basic"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-basic  [[elisp:(outline-show-subtree+toggle)][||]] /BpoRepo_BxeTree/  superClass=BpoRepo =A BPO Repository -- to be subclassed=  [[elisp:(org-cycle)][| ]]
#+end_org """
class BpoRepo_BxeTree(BpoRepo):
####+END:
    """
** Abstraction of the base ByStar Portable Object
"""
    def __init__(
            self,
            bpoId,
    ):
        super().__init__(bpoId)
        if not EffectiveBpos.givenBpoIdGetBpo(bpoId):
            b_io.eh.critical_usageError(f"Missing BPO for {bpoId}")
            return

    def info(self,):
        print("bxeTreeInfo")


####+BEGIN: bx:cs:py3:section :title "Common Parameters Specification"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *Common Parameters Specification*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: bx:dblock:python:func :funcName "commonParamsSpecify" :funcType "ParSpec" :retType "" :deco "" :argsList "csParams"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-ParSpec  [[elisp:(outline-show-subtree+toggle)][||]] /commonParamsSpecify/ retType= argsList=(csParams)  [[elisp:(org-cycle)][| ]]
#+end_org """
def commonParamsSpecify(
    csParams,
):
####+END:
    csParams.parDictAdd(
        parName='bpoRepoName',
        parDescription="Bx Portable ObjectId",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        argparseShortOpt=None,
        argparseLongOpt='--bpoRepoName',
    )

####+BEGIN: bx:cs:py3:section :title "CS-Lib Examples"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *CS-Lib Examples*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:func/typing :funcName "examples_csu" :funcType "eType" :retType "" :deco "default" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-eType  [[elisp:(outline-show-subtree+toggle)][||]] /examples_csu/  deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def examples_csu(
####+END:
        sectionTitle: typing.AnyStr = '',
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Examples of Service Access Instance Commands.
    #+end_org """

    # cmndOutcome = b.op.Outcome()

    od = collections.OrderedDict
    cmnd = cs.examples.cmndEnter

    if sectionTitle == 'default':
        cs.examples.menuChapter('*CMDB Container FileParams Access And Management --- Applicable To BPO Containers*')

    thisBpoId = "pmp_HSS-1012"
    thisEnvRelPath = 'cmdb/describe'

    cmnd('bpoRepo_gitDo', pars=od([('bpoId', thisBpoId), ('envRelPath', thisEnvRelPath)]), args="getExamples")
    cmnd('bpoRepo_gitDo', pars=od([('bpoId', thisBpoId), ('envRelPath', thisEnvRelPath)]), args="setExamples")


    cs.examples.menuChapter('*List repos for bpos*')


    cmnd('bpoReposNameList', wrapper="bpoAcctManage.sh -i bpoIdsList |", args="getExamples")

####+BEGIN: bx:dblock:python:section :title "ICM Commands"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ICM Commands*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "bpoRepo_gitAction" :comment "Returns the type of bpoId" :parsMand "bpoId" :parsOpt "" :argsMin 1 :argsMax 1 :pyInv "stdinArgs"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<bpoRepo_gitAction>>  *Returns the type of bpoId*  =verify= parsMand=bpoId argsMin=1 argsMax=1 ro=cli pyInv=stdinArgs   [[elisp:(org-cycle)][| ]]
#+end_org """
class bpoRepo_gitAction(cs.Cmnd):
    cmndParamsMandatory = [ 'bpoId', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             bpoId: typing.Optional[str]=None,  # Cs Mandatory Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
             stdinArgs: typing.Any=None,   # pyInv Argument
    ) -> b.op.Outcome:
        """Returns the type of bpoId"""
        failed = b_io.eh.badOutcome
        callParamsDict = {'bpoId': bpoId, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
        bpoId = csParam.mappedValue('bpoId', bpoId)
####+END:

        cmndArgsSpecDict = self.cmndArgsSpec()

        action = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)
        actionArgs = self.cmndArgsGet("1&9999", cmndArgsSpecDict, argsList)

        #fpsBase = os.path.join(bpo.bpoBaseDir_obtain(bpoId), envRelPath)

        basedFps = b.pattern.sameInstance(CmdbCntnr_FPs, bpoId, envRelPath)

        fpsBase = basedFps.basePath_obtain()

        if action == "getExamples" or action == "setExamples":
            # print(f"With fpBase={fpsBase} and cls={CmdbCntnr_FPs} name={basedFps.__class__.__name__}.")
            if b.fpCls.fpParamsReveal(cmndOutcome=cmndOutcome).cmnd(
                    rtInv=rtInv,
                    cmndOutcome=cmndOutcome,
                    fpBase=fpsBase,
                    cls=basedFps.__class__.__name__,
                    argsList=[action],
            ).isProblematic(): return(b_io.eh.badOutcome(cmndOutcome))

        elif action == "menu":
            print(f"With fpBase={fpsBase} and cls={CmdbCntnr_FPs} NOTYET.")
        else:
            print(f"bad input {action}")

        return(cmndOutcome)


####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default   [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """  #+begin_org
** [[elisp:(org-cycle)][| *cmndArgsSpec:* | ]]
        #+end_org """

        cmndArgsSpecDict = cs.arg.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="action",
            argChoices=['getExamples', 'setExamples',],
            argDescription="Action to be specified by rest"
        )

        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "bpoReposNameList" :comment "For each bpoId, list its repos" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 9999 :pyInv "pyStdinArgs"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<bpoReposNameList>>  *For each bpoId, list its repos*  =verify= argsMax=9999 ro=cli pyInv=pyStdinArgs   [[elisp:(org-cycle)][| ]]
#+end_org """
class bpoReposNameList(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 9999,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
             pyStdinArgs: typing.Any=None,   # pyInv Argument
    ) -> b.op.Outcome:
        """For each bpoId, list its repos"""
        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] This is an example of a CmndSvc with lots of features.
The features include:

        1) An optional parameter called someParam
        2) A first mandatory argument called action which must be one of list or print.
        3) An optional set of additional argumets.

The param, and args are then validated and form a single string.
That string is then echoed in a sub-prococessed. The stdout of that sub-proc is assigned
to a variable similar to bash back-quoting.

And that variable is then printed.

Variations of this are captured as snippets to be used.
        #+end_org """)

        self.captureRunStr(""" #+begin_org
#+begin_src sh :results output :session shared
  csExamples.cs --par1Example="par1Mantory" --par2Example="par2Optional" -i parsArgsStdinCmndResult arg1 argTwo
#+end_src
#+RESULTS:
:
: cmndArgs= arg1  argTwo
: stdin instead of methodInvokeArg =
: cmndParams= par1Mantory par2Optional
: OpError.Success
        #+end_org """)
        if self.justCaptureP(): return cmndOutcome

        def processEach(each):
            print(f"""bxoGitlab.py -v 30 --bpoId={each} -i reposList""")

####+BEGIN: b:py3:func/processArgsAndStdin :comment auto-generated
        """ #+begin_org
***  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  processArgsAndStdin [[elisp:(outline-show-subtree+toggle)][||]]  =auto-generated=  [[elisp:(org-cycle)][| ]]
        #+end_org """
        if not pyStdinArgs:
            pyStdinArgs = b_io.stdin.read()

        def processArgsAndStdin():
            cmndArgsSpecDict = self.cmndArgsSpec()
            cliArgs = self.cmndArgsGet("0&9999", cmndArgsSpecDict, argsList)

            effectiveArgs = cliArgs + pyStdinArgs.split()

            if len(effectiveArgs) == 0:
                b_io.eh.critical_usageError("Missing Input: One of cliArgs, stdin or pyArgs; should have an input.")

            for each in effectiveArgs:
                processEach(each)

        processArgsAndStdin()

####+END:

        return(cmndOutcome)


####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default   [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """  #+begin_org
** [[elisp:(org-cycle)][| *cmndArgsSpec:* | ]]
        #+end_org """

        cmndArgsSpecDict = cs.arg.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&9999",
            argName="actionArgs",
            argChoices=[],
            argDescription="Rest of args for use by action"
        )

        return cmndArgsSpecDict



####+BEGIN: b:py3:cs:framework/endOfFile :basedOn "classification"
""" #+begin_org
* [[elisp:(org-cycle)][| *End-Of-Editable-Text* |]] :: emacs and org variables and control parameters
#+end_org """

#+STARTUP: showall

### local variables:
### no-byte-compile: t
### end:
####+END:
