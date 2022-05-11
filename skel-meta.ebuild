# Copyright 1999-2022 Gentoo Authors
# Distributed under the terms of the GNU General Public License v2

EAPI=8

DESCRIPTION="<{DESCRIPTION}>"
HOMEPAGE="https://octave.sourceforge.io"

LICENSE="GPL-3"
SLOT="0"
KEYWORDS="~amd64 ~arm ~arm64 ~ppc ~ppc64 ~riscv ~x86"

RDEPEND="
<% for PKG in PKG_LIST %>
	<{ PKG }>
<% endfor %>
"

DEPEND="${RDEPEND}"

pkg_postinst() {
	elog "Please append these to ~/.octaverc"
<% for PKG in PKG_LIST %>
	elog "pkg load <{ PKG | replace("sci-mathematics/octave-", "") }>"
<% endfor %>
}

pkg_postrm() {
	elog "Please remove these from ~/.octaverc"
<% for PKG in PKG_LIST %>
	elog "pkg load <{ PKG | replace("sci-mathematics/octave-", "") }>"
<% endfor %>
}
