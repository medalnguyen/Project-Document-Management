import wx
import wx.grid as gridlib

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="POSync - Dashboard", size=(1000, 600))

        # Set window icon
        self.SetIcon(wx.Icon(r"D:\Promgramming\Project-Document-Management\App\icon\icon_tilte.ico", wx.BITMAP_TYPE_ICO))
        
        # Menu
        self._create_menu_bar()

        # Status bar
        self.CreateStatusBar()
        self.SetStatusText("Sẵn sàng")

        # Main panel
        main_panel = wx.Panel(self)
        main_panel.SetBackgroundColour("#B1D4E0")
        # -------------------------------------------------------
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # -------------------------------------------------------
        # -------------------- Toolbar Panel --------------------
        # -------------------------------------------------------
        toolbar_panel = wx.Panel(main_panel)
        toolbar_panel.SetBackgroundColour("#B1D4E0")
        toolbar_sizer = wx.BoxSizer(wx.HORIZONTAL)
        btn_load = wx.Button(toolbar_panel, label="📂 Load", size=(120, 40))
        btn_import = wx.Button(toolbar_panel, label="⬆ Import", size=(120, 40))
        btn_export = wx.Button(toolbar_panel, label="⬇ Export", size=(120, 40))
        toolbar_sizer.Add(btn_load, 0, wx.ALL, 4)
        toolbar_sizer.Add(btn_import, 0, wx.ALL, 4)
        toolbar_sizer.Add(btn_export, 0, wx.ALL, 4)
        # Thêm text "Commissioning"
        commissioning_text = wx.StaticText(toolbar_panel, label="Commissioning Team")
        commissioning_text.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        commissioning_text.SetForegroundColour("#000000")  # Đổi màu chữ tại đây
        toolbar_sizer.Add(commissioning_text, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 120)
        # Thêm icon
        toolbar_sizer.AddStretchSpacer()
        icon_img = wx.Image(r"D:\Promgramming\Project-Document-Management\App\icon\icon_toolbar.ico", wx.BITMAP_TYPE_ICO)
        icon_img = icon_img.Scale(50, 50, wx.IMAGE_QUALITY_HIGH)
        icon_bitmap = wx.Bitmap(icon_img)
        toolbar_icon = wx.StaticBitmap(toolbar_panel, bitmap=icon_bitmap)
        toolbar_sizer.Add(toolbar_icon, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 12)
        # Kết thúc code Toolbar
        toolbar_panel.SetSizer(toolbar_sizer)
        main_sizer.Add(toolbar_panel, 0, wx.EXPAND | wx.ALL, 5)

        # ----------------------------------------------------
        # -------------------- Body Panel --------------------
        # ----------------------------------------------------
        body_panel = wx.Panel(main_panel)
        body_panel.SetBackgroundColour("#B1D4E0")
        # ----------------------------------------------------
        body_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # ------------------- Sidebar --------------------
        sidebar_panel = wx.Panel(body_panel, size=(180, -1))
        sidebar_panel.SetBackgroundColour("#2E8BC0")
        sidebar_sizer = wx.BoxSizer(wx.VERTICAL)
        # Tạo TreeCtrl
        self.tree = wx.TreeCtrl(
            sidebar_panel,
            style=wx.TR_HAS_BUTTONS | wx.TR_HIDE_ROOT | wx.HSCROLL | wx.VSCROLL
        )
        self.tree.SetBackgroundColour("#FFFFFF")
        # Root ẩn
        root = self.tree.AddRoot("View")
        for item in ["Checksheet Overview", "Certificate Overview", "Punch List Overview", "FTP Overview"]:
            self.tree.AppendItem(root, item)
        sidebar_sizer.Add(self.tree, 1, wx.EXPAND | wx.ALL, 5)
        sidebar_panel.SetSizer(sidebar_sizer)
        body_sizer.Add(sidebar_panel, 0, wx.EXPAND | wx.ALL, 5)

        #------------------- Content --------------------
        content_panel = wx.Panel(body_panel)
        content_panel.SetBackgroundColour("#2E8BC0")
        content_sizer = wx.BoxSizer(wx.VERTICAL)
        self.grid = gridlib.Grid(content_panel)
        self.grid.CreateGrid(10, 5)
        col_labels = ["File Name", "Size", "Type", "Date Modified", "Status"]
        for idx, label in enumerate(col_labels):
            self.grid.SetColLabelValue(idx, label)
        content_sizer.Add(self.grid, 1, wx.EXPAND | wx.ALL, 8)
        log_box = wx.StaticBox(content_panel, label="Logs")
        log_sizer = wx.StaticBoxSizer(log_box, wx.VERTICAL)
        self.log_ctrl = wx.TextCtrl(content_panel, style=wx.TE_MULTILINE | wx.TE_READONLY, size=(-1, 120))
        log_sizer.Add(self.log_ctrl, 1, wx.EXPAND | wx.ALL, 5)
        content_sizer.Add(log_sizer, 0, wx.EXPAND | wx.ALL, 8)
        content_panel.SetSizer(content_sizer)
        body_sizer.Add(content_panel, 1, wx.EXPAND | wx.ALL, 5)

        body_panel.SetSizer(body_sizer)
        main_sizer.Add(body_panel, 1, wx.EXPAND)
        main_panel.SetSizer(main_sizer)

        # Events
        btn_load.Bind(wx.EVT_BUTTON, self.on_load)
        btn_import.Bind(wx.EVT_BUTTON, self.on_import)
        btn_export.Bind(wx.EVT_BUTTON, self.on_export)

        self.Show()

    #--------------------Functions--------------------

    def _create_menu_bar(self):
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        mi_exit = file_menu.Append(wx.ID_EXIT, 'E&xit\tCtrl-Q', 'Thoát chương trình')
        self.Bind(wx.EVT_MENU, self.on_exit, mi_exit)

        help_menu = wx.Menu()
        mi_about = help_menu.Append(wx.ID_ABOUT, '&About\tF1', 'Thông tin')
        self.Bind(wx.EVT_MENU, self.on_about, mi_about)

        menu_bar.Append(file_menu, '&File')
        menu_bar.Append(help_menu, '&Help')
        self.SetMenuBar(menu_bar)

    def on_load(self, event):
        self.log_ctrl.AppendText("Load clicked\n")
        self.SetStatusText("Load action")

    def on_import(self, event):
        dlg = wx.FileDialog(self, "Open file", wildcard="All files (*.*)|*.*",
                            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.log_ctrl.AppendText(f"Imported: {path}\n")
            self.SetStatusText(f"Imported: {path}")
        dlg.Destroy()

    def on_export(self, event):
        dlg = wx.FileDialog(self, "Save file", wildcard="All files (*.*)|*.*",
                            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.log_ctrl.AppendText(f"Exported: {path}\n")
            self.SetStatusText(f"Exported: {path}")
        dlg.Destroy()

    def on_about(self, event):
        wx.MessageBox("POSync Dashboard\nAuthor: Ego", "About", wx.OK | wx.ICON_INFORMATION)

    def on_exit(self, event):
        self.Close()

if __name__ == '__main__':
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()
