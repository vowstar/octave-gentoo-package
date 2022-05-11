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
