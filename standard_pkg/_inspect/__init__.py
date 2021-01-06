# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
import inspect
from pprint import pprint

__all_function = [f for f in dir(inspect) if inspect.isfunction(getattr(inspect, f))]
pprint(__all_function)

funcs = ['_check_class',
         '_check_instance',
         '_findclass',
         '_finddoc',
         '_getfullargs',
         '_is_type',
         '_main',
         '_missing_arguments',
         '_shadowed_dict',
         '_signature_bound_method',
         '_signature_from_builtin',
         '_signature_from_callable',
         '_signature_from_function',
         '_signature_fromstr',
         '_signature_get_bound_param',
         '_signature_get_partial',
         '_signature_get_user_defined_method',
         '_signature_is_builtin',
         '_signature_is_functionlike',
         '_signature_strip_non_python_syntax',
         '_static_getmro',
         '_too_many',
         'classify_class_attrs',
         'cleandoc',
         'currentframe',
         'findsource',
         'formatannotation',
         'formatannotationrelativeto',
         'formatargspec',
         'formatargvalues',
         'getabsfile',
         'getargs',
         'getargspec',
         'getargvalues',
         'getattr_static',
         'getblock',
         'getcallargs',
         'getclasstree',
         'getclosurevars',
         'getcomments',
         'getcoroutinelocals',
         'getcoroutinestate',
         'getdoc',
         'getfile',
         'getframeinfo',
         'getfullargspec',
         'getgeneratorlocals',
         'getgeneratorstate',
         'getinnerframes',
         'getlineno',
         'getmembers',
         'getmodule',
         'getmodulename',
         'getmro',
         'getouterframes',
         'getsource',
         'getsourcefile',
         'getsourcelines',
         'indentsize',
         'isabstract',
         'isasyncgen',
         'isasyncgenfunction',
         'isawaitable',
         'isbuiltin',
         'isclass',
         'iscode',
         'iscoroutine',
         'iscoroutinefunction',
         'isdatadescriptor',
         'isframe',
         'isfunction',
         'isgenerator',
         'isgeneratorfunction',
         'isgetsetdescriptor',
         'ismemberdescriptor',
         'ismethod',
         'ismethoddescriptor',
         'ismodule',
         'isroutine',
         'istraceback',
         'namedtuple',
         'signature',
         'stack',
         'trace',
         'unwrap',
         'walktree']