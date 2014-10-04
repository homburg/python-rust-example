use std::c_str::CString;

#[no_mangle]
pub extern "C" fn it_works(input: *const i8, j: int) {
	let unsafe_str = unsafe {
		CString::new(input, false)
	};
	let str = match unsafe_str.as_str() {
		Some(utf8_str) => utf8_str,
		None => {
			println!("Invalid utf-8");
			""
		},
	};
	println!("Hello, rust! say: {} ({})", str, j);
}
