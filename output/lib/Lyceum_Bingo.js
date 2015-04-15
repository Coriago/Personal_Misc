/* start module: Lyceum_Bingo */
$pyjs['loaded_modules']['Lyceum_Bingo'] = function (__mod_name__) {
	if($pyjs['loaded_modules']['Lyceum_Bingo']['__was_initialized__']) return $pyjs['loaded_modules']['Lyceum_Bingo'];
	var $m = $pyjs['loaded_modules']['Lyceum_Bingo'];
	$m['__repr__'] = function() { return '<module: Lyceum_Bingo>'; };
	$m['__was_initialized__'] = true;
	if ((__mod_name__ === null) || (typeof __mod_name__ == 'undefined')) __mod_name__ = 'Lyceum_Bingo';
	$m['__name__'] = __mod_name__;
	var $add2,$iter2_nextval,$iter2_type,$iter2_iter,$iter2_idx,$add1,$sub2,$sub1,$iter2_array;

	$m['sys'] = $p['___import___']('sys', null);
	$p['__import_all__']('PySide.QtCore', null, $m, null, false);
	$p['__import_all__']('PySide.QtGui', null, $m, null, false);
	$m['random'] = $p['___import___']('random', null);
	$m['nums'] = $p['list']([]);
	$m['app'] = (typeof QApplication == "undefined"?$m['QApplication']:QApplication)($p['getattr']($m['sys'], 'argv'));
	$m['is_duplicate'] = function(l, r) {
		var $iter1_nextval,$iter1_type,$iter1_iter,$iter1_array,n,$iter1_idx;
		$iter1_iter = l;
		$iter1_nextval=$p['__iter_prepare']($iter1_iter,false);
		while (typeof($p['__wrapped_next']($iter1_nextval)['$nextval']) != 'undefined') {
			n = $iter1_nextval['$nextval'];
			if ($p['bool']($p['op_eq'](r, n))) {
				return true;
			}
		}
		return false;
	};
	$m['is_duplicate']['__name__'] = 'is_duplicate';

	$m['is_duplicate']['__bind_type__'] = 0;
	$m['is_duplicate']['__args__'] = [null,null,['l'],['r']];
	$iter2_iter = $p['range'](24);
	$iter2_nextval=$p['__iter_prepare']($iter2_iter,false);
	while (typeof($p['__wrapped_next']($iter2_nextval)['$nextval']) != 'undefined') {
		$m['n'] = $iter2_nextval['$nextval'];
		$m['randNum'] = $m['random']['randint'](1, 300);
		if ($p['bool']($p['op_eq']($m['is_duplicate']($m['nums'], $m['randNum']), true))) {
			$m['n'] = $p['__op_sub']($sub1=$m['n'],$sub2=1);
		}
		else {
			$m['nums']['append']($m['randNum']);
		}
	}
	$m['$$label'] = (typeof QLabel == "undefined"?$m['QLabel']:QLabel)($p['__op_add']($add1=$p['str']($m['nums']),$add2='\n'));
	$m['$$label']['show']();
	$m['app']['exec_']();
	$m['sys']['exit']();
	return this;
}; /* end Lyceum_Bingo */


/* end module: Lyceum_Bingo */


/*
PYJS_DEPS: ['sys', 'PySide.QtCore', 'PySide', 'PySide.QtGui', 'random']
*/
