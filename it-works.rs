use std::c_str::CString;

#[no_mangle]
pub extern "C" fn it_works(input: *const i8, j: int) {
	let unsafe_str = unsafe {
		CString::new(input, false)
	};
	let str = unsafe_str.as_str().unwrap();
	println!("Hello, rust! say: {} ({})", str, j);
}
