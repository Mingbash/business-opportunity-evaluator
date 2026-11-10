from pathlib import Path
import importlib.util, json, shutil, sys, tempfile, unittest, zipfile
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('checker',ROOT/'scripts/check_release.py')
checker=importlib.util.module_from_spec(spec);spec.loader.exec_module(checker)

class PackageTests(unittest.TestCase):
    def test_legacy_name_has_the_same_evaluation_instructions(self):
        canonical=ROOT/'skills/idea-validation'
        legacy=ROOT/'skills/business-opportunity-evaluator'
        files={p.relative_to(canonical) for p in canonical.rglob('*') if p.is_file()}
        self.assertEqual(files,{p.relative_to(legacy) for p in legacy.rglob('*') if p.is_file()})
        for path in files:
            with self.subTest(path=path):
                expected=(legacy/path).read_text().replace('business-opportunity-evaluator','idea-validation').replace('Business Opportunity Evaluator','Idea Validation')
                self.assertEqual((canonical/path).read_text(),expected)
    def test_release_manifest_includes_both_complete_skills(self):
        manifest=json.loads((ROOT/'release-files.json').read_text())
        self.assertEqual(len(manifest),len(set(manifest)))
        for skill in (ROOT/'skills').iterdir():
            files={str(p.relative_to(ROOT)) for p in skill.rglob('*') if p.is_file()}
            self.assertEqual(files,{p for p in manifest if p.startswith('skills/'+skill.name+'/')})
    def test_both_archive_names_install_independently(self):
        sys.path.insert(0,str(ROOT/'scripts'))
        try:
            import package_release
            with tempfile.TemporaryDirectory() as tmp:
                out=Path(tmp)/'archives'
                package_release.build(out)
                for name in ('idea-validation','business-opportunity-evaluator'):
                    with self.subTest(name=name),tempfile.TemporaryDirectory() as install:
                        with zipfile.ZipFile(out/f'{name}-{package_release.VERSION}.zip') as archive:
                            archive.extractall(install)
                        self.assertEqual(checker.check_skill(Path(install)/name),[])
                        self.assertIn(f'name: {name}\n',(Path(install)/name/'SKILL.md').read_text())
        finally:
            sys.path.pop(0)
    def test_each_skill_is_standalone(self):
        for skill in (ROOT/'skills').iterdir():
            with self.subTest(skill=skill.name),tempfile.TemporaryDirectory() as tmp:
                isolated=Path(tmp)/skill.name;shutil.copytree(skill,isolated)
                self.assertEqual(checker.check_skill(isolated),[])
    def test_collection_has_no_broken_links_or_shared_drift(self):
        self.assertEqual(checker.check(),[])
    def test_standalone_checker_rejects_sibling_dependency(self):
        with tempfile.TemporaryDirectory() as tmp:
            s=Path(tmp)/'demo';s.mkdir();(s/'SKILL.md').write_text('---\nname: demo\ndescription: Example\n---\n[bad](../sibling/rules.md)')
            self.assertTrue(checker.check_skill(s))

if __name__=='__main__':unittest.main()
